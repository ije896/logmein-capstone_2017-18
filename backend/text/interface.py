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
        self.stt_script = None # Speech to text script
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

        #self.stt_script = Interface.check_file(fp) # Passing stt as string and not file now
        self.stt_script = fp

        for (opt, val) in options.items():
            print("(opt, val) = ({}, {})".format(opt, val))
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

        results = {}
        if st:
            sent_dict = Interface.get_sentiment(self.stt_script)
            results['sentiment'] = sent_dict

        if sy:
            syn_list  = Interface.get_synonyms(self.stt_script, self.syn_dict)
            results['synonyms'] = syn_list

        if r:
            read_dict = Interface.get_readability(self.stt_script)
            results['readability'] = read_dict

        if art:
            results['articulation'] = Interface.get_articulation("../research/{}".format(challenge_id), "../research/{}.stt".format(challenge_id))

        return results

    @staticmethod
    def get_sentiment(stt_script):
        tones = watson.WatsonAnalyzer.get_sentiment(stt_script)
        sentiment = {'sentiment': tones}
        return sentiment

    @staticmethod
    def get_synonyms(stt_script, syn):
        tfidf = tf_idf.TfIdf.get_tf_idf(stt_script)

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
    def get_readability(stt_script):
        score = readability.Readability.f_k(stt_script)
        grade = readability.Readability.f_k_grade_level(stt_script)

        read_list = {'score': score, 'grade': grade}
        read = {'readability': read_list}
        return read

    @staticmethod
    def get_articulation(trs_path, stt):
        return articulation.Articulation.get_articulation_str(trs_path, stt)

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
