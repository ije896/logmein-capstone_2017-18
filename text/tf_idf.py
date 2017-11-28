from decimal import *
from string import punctuation


# Reads in from csv file for use in calculating tf_idf
# TODO: remove numbers (we have words like 2146 in corpus)
# TODO: do we even need len(corpus)? [probably not, remove eventually]

class TfIdf:

    @staticmethod
    def parse_freqs(freqs_csv):
        freqs = {}
        with open(freqs_csv, 'r') as csv:
            first = csv.readline()
            rest = csv.readlines()

            (sentinel, length) = first.rstrip().split(',')
            assert (sentinel == "len(corpus)")

            for line in rest:
                (word, f) = line.strip().split(',')
                freqs[word] = int(f)
        return freqs

    @staticmethod
    def parse_idfs(idf_csv):
        idfs = {}
        with open(idf_csv, 'r') as csv:
            for line in csv.readlines():
                (word, idf) = line.strip().split(',')
                idfs[word] = float(idf)
        return idfs


    '''
	Text frequency  - inverse corpus frequency
	equivalent to freq(word) / [ corpus_freq(word) / len(corpus) ]
	'''

    # We use the Decimal library to preserve arbitrary precision
    # TODO: decide if we want to ignore words not in the corpus or instead do something like freqs.get(w, .25)

    @staticmethod
    def tf_cf(text, freqs):
        stripped_text = TfIdf.strip_punctuation(text)
        text_words = stripped_text.split(' ')
        tfcf = []
        for w in text_words:
            w = w.lower()
            (ct, cf) = (Decimal(stripped_text.count(w)), Decimal(freqs.get(w, 0)))
            assert (ct > 0)

            if cf == 0:  # Word does not appear in corpus, ignore it for now
                continue
            tfcf.append((w, ct / cf))

        # Remove duplicates
        tfcf = list(set(tfcf))

        return sorted(tfcf, key=lambda tup: tup[1], reverse=True)

    @staticmethod
    def tf_idf(text, idfs):
        stripped_text = TfIdf.strip_punctuation(text)
        text_words = stripped_text.split(' ')
        tfidf = []
        for w in text_words:
            w = w.lower()
            (ct, idf) = (Decimal(stripped_text.count(w)), Decimal(idfs.get(w, 0)))
            assert (ct > 0)

            if idf == 0:  # Word appears in all corpus documents so we don't care
                continue
            tfidf.append((w, ct * idf))

        # Remove duplicates
        tfidf = list(set(tfidf))

        return sorted(tfidf, key=lambda tup: tup[1], reverse=True)

    # Strip punctuation from text, only want words
    # Also place all letters to lower case to avoid duplication
    @staticmethod
    def strip_punctuation(text):
        # Set up translation table for use with string.translate(translator)
        translator = str.maketrans('', '', punctuation)

        text = text.replace('\n', ' ')

        stripped_text = []
        for item in text.split(' '):
            word = item.lower().translate(translator).strip()
            if len(word) > 1:
                stripped_text.append(word)
        return ' '.join(stripped_text)


    @staticmethod
    def get_tf_idf(text):
        idf_csv   = "text/corp_idf_brown.csv"  # TODO: make permanent location

        idfs = TfIdf.parse_idfs(idf_csv)

        tf_idf_list = TfIdf.tf_idf(text, idfs)

        tf_idf = [word for (word, count) in tf_idf_list]

        return tf_idf

    @staticmethod
    def get_tf_cf(text):
        freqs_csv = "text/corp_freq_brown.csv"  # TODO: make permanent location

        freqs = TfIdf.parse_freqs(freqs_csv)

        tf_cf_list = TfIdf.tf_idf(text, freqs)

        tf_cf = [word for (word, count) in tf_cf_list]

        return tf_cf

