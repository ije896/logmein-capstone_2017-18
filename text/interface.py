#!/usr/bin/env python3

import os
import sys
import json

from text import text_analysis


class Interface:
    def __init__(self):
        self.st  = False
        self.sy  = False
        self.r   = False

    # Make a dictionary of features as booleans
    def processFilepath(self, text, options):
        ta = text_analysis.TextAnalysis(text)

        for (opt, val) in options.items():
            if val:
                if opt == "run_all":
                    self.st = True
                    self.sy = True
                    self.r  = True
                    break
                elif opt == "sentiment":
                    self.st = True
                elif opt == "synonyms":
                    self.sy = True
                elif opt == "readability":
                    self.r = True
                else:
                    print("ERROR: Options are {run_all, sentiment, synonyms, readability}")
                    exit(1)

        json_list = []
        if self.st:
            sentiment = ta.get_sentiment()
            json_list.append(sentiment)

        if self.sy and self.st:
            synonyms = ta.get_synonyms()
            json_list.append(synonyms)

        if self.r:
            readability = ta.get_readability()
            json_list.append(readability)

        self.json = json.dumps(json_list, indent=2)
        return self.json