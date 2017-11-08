from decimal import *


# Reads in from csv file for use in calculating tf_idf
# TODO: remove numbers (we have words like 2146 in corpus)
# TODO: do we even need len(corpus)?

class tf_idf:
    def __init__(self):
        self.freqs_csv = "corp_freq_brown.csv"  # TODO: add Text_Analysis/ before file
        self.idf_csv   = "corp_idf_brown.csv"   # TODO: add Text_Analysis/ before file

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
    def tf_icf(self, text):
        text_words = text.split(' ')
        tficf = []
        for w in text_words:
            w = w.lower()
            (ct, cf) = (Decimal(text.count(w)), Decimal(self.freqs.get(w, 0)))
            assert (ct > 0)

            if cf == 0:  # Word does not appear in corpus, ignore it for now
                continue
            tficf.append((w, ct / cf))
        # print("tf_icf(): (w, ct / cf) = ({}, {})".format( w, ct/cf ))

        return sorted(tficf, key=lambda tup: tup[1], reverse=True)

    def tf_idf(self, text):
        text_words = text.split(' ')
        tfidf = []
        for w in text_words:
            w = w.lower()
            (ct, idf) = (Decimal(text.count(w)), Decimal(self.idfs.get(w, 0)))
            assert (ct > 0)

            if idf == 0:  # Word appears in all corpus documents so we don't care
                continue
            tfidf.append((w, ct * idf))
        # print("tf_icf(): (w, ct / cf) = ({}, {})".format( w, ct/cf ))

        return sorted(tfidf, key=lambda tup: tup[1], reverse=True)


if __name__ == '__main__':
    test = tf_idf()
    test1 = test.tf_icf("I have a dream that one day this nation will rise up")
    for x in test1:
        print("(w, ct/cf) = ({}, {})".format(x[0], x[1]))

    print("\n")
    test2 = test.tf_idf("I have a dream that one day this nation will rise up")
    for x in test2:
        print("(w, ct*idf) = ({}, {})".format(x[0], x[1]))

