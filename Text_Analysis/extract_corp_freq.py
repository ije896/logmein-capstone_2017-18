from string import punctuation
from nltk.corpus import brown

from collections import Counter # Nice library to make getting frequencies easy
import argparse

parser = argparse.ArgumentParser(description='Cleans up Brown corpus and writes to file')
parser.add_argument('output', nargs='?', type=argparse.FileType('w'), default='corp_freqs_brown.csv',
                    help='where to write the csv frequency output')

args = parser.parse_args()

# Set up translation table for use with string.translate(translator)
translator = str.maketrans('', '', punctuation)
 
words = brown.words()

corp_words = []
for w in words:
    word = w.lower().translate(translator).strip()

    if len(word) > 1:
        corp_words.append(word)
        #print("w = {}, len(w) = {}".format(word, len(word)))


# Vectorize by frequency

counts = Counter(corp_words)

# Write our vectorized result to csv
# Credit to https://stackoverflow.com/a/19739263/8829491 for csv.write one-liner
with args.output as csv:
	[csv.write('{0},{1}\n'.format(key, value)) for key, value in counts.items()]





