#!/usr/bin/env python3

import json

from text import synonyms
from text import readability
from text import articulation
from text import tf_idf
from text import watson


class Interface:
    def __init__(self):
        self.syn_dict = synonyms.Synonyms()
        self.tts_script = None
        self.act_script = None # Actual script (ex: for a challenge, this is the script we provide the user)

    # Make a dictionary of features as booleans
    def process_filepath(self, fp, options):
        challenge_id = options['challenge_id']

        if challenge_id is None:
            print("ERROR: No challenge_id provided. Exiting\n")
            return -1

        st  = False
        sy  = False
        r   = False
        art = False

        #self.tts_script = Interface.check_file(fp) # Passing tts as string and not file now
        self.tts_script = fp

        for (opt, val) in options.items():
            if val:
                if opt == "run_all":
                    st  = True
                    sy  = True
                    r   = True
                    art = True
                    break
                elif opt == "sentiment":
                    st = True
                elif opt == "synonyms":
                    sy = True
                elif opt == "readability":
                    r  = True
                elif opt == "art":
                    art = True
                else:
                    print("ERROR: Options are {run_all, sentiment, synonyms, readability, art}")
                    exit(1)

        json_list = []
        if st:
            sent_dict = Interface.get_sentiment(self.tts_script)
            json_list.append(sent_dict)

        if sy:
            syn_list  = Interface.get_synonyms(self.tts_script, self.syn_dict)
            json_list.append(syn_list)

        if r:
            read_dict = Interface.get_readability(self.tts_script)
            json_list.append(read_dict)

        if art:
            art_dict = {}
            art_dict[art] = Interface.get_articulation("../research/{}".format(challenge_id), "../research/{}.tts".format(challenge_id))
            json_list.append(art_dict)

        json_object = json.dumps(json_list, indent=2)
        return json_object

    @staticmethod
    def get_sentiment(tts_script):
        tones = watson.WatsonAnalyzer.get_sentiment(tts_script)
        sentiment = {'sentiment': tones}
        return sentiment

    @staticmethod
    def get_synonyms(tts_script, syn):
        tfidf = tf_idf.TfIdf.get_tf_idf(tts_script)

        syns = {}
        idf_index = 0
        while len(syns) < 5 and idf_index < len(tfidf):
            word = tfidf[idf_index]
            synonym = syn.get_syns(word)
            if synonym != -1:
                syns[word] = synonym
            idf_index += 1
        syn_list = {'synonyms': syns}
        return syn_list

    @staticmethod
    def get_readability(tts_script):
        score = readability.Readability.f_k(tts_script)
        grade = readability.Readability.f_k_grade_level(tts_script)

        read_list = {'score': score, 'grade': grade}
        read = {'readability': read_list}
        return read

    @staticmethod
    def get_articulation(trs_path, tts):
        return articulation.Articulation.get_articulation_str(trs_path, tts)

    @staticmethod
    def output_readability_tests():
        readability.Readability.output_tests()

    @staticmethod
    def check_file(fp):
        #Try to open it as a file
        try:
            file_object = open(fp, 'r')
            text = file_object.read()
            file_object.close()
            return text
        except:
            return fp
