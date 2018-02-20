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
        self.script   = None

    # Make a dictionary of features as booleans
    def process_filepath(self, fp, options):
        st  = False
        sy  = False
        r   = False
        art = False

        self.script = Interface.check_file(fp)

        for (opt, val) in options.items():
            if val:
                if opt == "run_all":
                    st = True
                    sy = True
                    r  = True
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
                    print("ERROR: Options are {run_all, sentiment, synonyms, readability}")
                    exit(1)

        json_list = []
        if st:
            sent_dict = Interface.get_sentiment(self.script)
            json_list.append(sent_dict)

        if sy:
            syn_list  = Interface.get_synonyms(self.script, self.syn_dict)
            json_list.append(syn_list)

        if r:
            read_dict = Interface.get_readability(self.script)
            json_list.append(read_dict)

        if art:
            art_dict = {}
            art_dict['art'] = Interface.get_articulation("research/enigma_tc_transcript.txt", "research/rkemper_take2_transcript_actual.txt")
            json_list.append(art_dict)

        json_object = json.dumps(json_list, indent=2)
        return json_object

    @staticmethod
    def get_sentiment(script):
        tones = watson.WatsonAnalyzer.get_sentiment(script)
        sentiment = {'sentiment': tones}
        return sentiment

    @staticmethod
    def get_synonyms(script, syn):
        tfidf = tf_idf.TfIdf.get_tf_idf(script)

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
    def get_readability(script):
        score = readability.Readability.f_k(script)
        grade = readability.Readability.f_k_grade_level(script)

        read_list = {'score': score, 'grade': grade}
        read = {'readability': read_list}
        return read

    @staticmethod
    # TODO: fix me cause we won't want to 
    def get_articulation(trs_path, tts_path):
        return articulation.Articulation.get_articulation(trs_path, tts_path)

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
