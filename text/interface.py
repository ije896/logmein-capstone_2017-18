#!/usr/bin/env python3

import os
import sys
import json

from text import text_analysis


class Interface:

    # Make a dictionary of features as booleans
    @staticmethod
    def process_filepath(text, options):
        st = False
        sy = False
        r = False
        ta = text_analysis.TextAnalysis(text)

        for (opt, val) in options.items():
            if val:
                if opt == "run_all":
                    st = True
                    sy = True
                    r  = True
                    break
                elif opt == "sentiment":
                    st = True
                elif opt == "synonyms":
                    sy = True
                elif opt == "readability":
                    r = True
                else:
                    print("ERROR: Options are {run_all, sentiment, synonyms, readability}")
                    exit(1)

        json_list = []
        if st:
            sentiment = ta.get_sentiment()
            json_list.append(sentiment)

        if sy:
            synonyms = ta.get_synonyms()
            json_list.append(synonyms)

        if r:
            readability = ta.get_readability()
            json_list.append(readability)

        json_object = json.dumps(json_list, indent=2)
        return json_object