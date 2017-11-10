from decimal import *
from string import punctuation


# Reads in from csv file for use in calculating tf_idf
# TODO: remove numbers (we have words like 2146 in corpus)
# TODO: do we even need len(corpus)?

class tf_idf:
    def __init__(self):
        self.freqs_csv = "/Users/zacharyfeinn/Repos/logmein-capstone_2017-18/Text_Analysis/corp_freq_brown.csv"  # TODO: add Text_Analysis/ before file
        self.idf_csv   = "/Users/zacharyfeinn/Repos/logmein-capstone_2017-18/Text_Analysis/corp_idf_brown.csv"   # TODO: add Text_Analysis/ before file

        self.len_corp = 0
        self.freqs = {}
        self.idfs  = {}
        self.parse_freqs()
        self.parse_idfs()

    def parse_freqs(self):
        with open(self.freqs_csv, 'r') as csv:
            first = csv.readline()
            rest = csv.readlines()

            (sentinel, length) = first.rstrip().split(',')
            assert (sentinel == "len(corpus)")
            self.len_corp = int(length)

            for line in rest:
                (word, f) = line.strip().split(',')
                self.freqs[word] = int(f)

    def parse_idfs(self):
        with open(self.idf_csv, 'r') as csv:
            for line in csv.readlines():
                (word, idf) = line.strip().split(',')
                self.idfs[word] = float(idf)


    '''
	Text frequency  - inverse corpus frequency
	equivalent to freq(word) / [ corpus_freq(word) / len(corpus) ]
	'''

    # We use the Decimal library to preserve arbitrary precision
    # TODO: decide if we want to ignore words not in the corpus or instead do something like freqs.get(w, .25)
    
    def tf_cf(self, text):
        stripped_text = self.strip_punctuation(text)
        text_words = stripped_text.split(' ')
        tfcf = []
        for w in text_words:
            w = w.lower()
            (ct, cf) = (Decimal(stripped_text.count(w)), Decimal(self.freqs.get(w, 0)))
            assert (ct > 0)

            if cf == 0:  # Word does not appear in corpus, ignore it for now
                continue
            tfcf.append((w, ct / cf))

        # Remove duplicates
        tfcf = list(set(tfcf))

        return sorted(tfcf, key=lambda tup: tup[1], reverse=True)

    def tf_idf(self, text):
        stripped_text = self.strip_punctuation(text)
        text_words = stripped_text.split(' ')
        tfidf = []
        for w in text_words:
            w = w.lower()
            (ct, idf) = (Decimal(stripped_text.count(w)), Decimal(self.idfs.get(w, 0)))
            assert (ct > 0)

            if idf == 0:  # Word appears in all corpus documents so we don't care
                continue
            tfidf.append((w, ct * idf))

        # Remove duplicates
        tfidf = list(set(tfidf))

        return sorted(tfidf, key=lambda tup: tup[1], reverse=True)

    # Strip punctuation from text, only want words
    # Also place all letters to lower case to avoid duplication 
    def strip_punctuation(self, text):
        # Set up translation table for use with string.translate(translator)
        translator = str.maketrans('', '', punctuation)

        text = text.replace('\n', ' ')

        stripped_text = []
        for item in text.split(' '):
            word = item.lower().translate(translator).strip()
            if len(word) > 1:
                stripped_text.append(word)
        return ' '.join(stripped_text)

    def get_tf_idf(self, text):
        tf_idf_list = self.tf_idf(text)
        tf_idf = [word for (word,count) in tf_idf_list]
        return tf_idf

    def get_tf_cf(self, text):
        tf_cf_list = self.tf_cf(text)
        tf_cf = [word for (word,count) in tf_cf_list]
        return tf_cf


