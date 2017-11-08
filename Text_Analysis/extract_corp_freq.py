from string import punctuation
from nltk.corpus import brown

from collections import Counter  # Nice library to make getting frequencies easy
import argparse
from math import log

parser = argparse.ArgumentParser(description='Cleans up Brown corpus and writes freqs to file')
parser.add_argument('freq_output', nargs='?', type=argparse.FileType('w'), default='corp_freq_brown.csv',
                    help='where to write the csv frequency output')
parser.add_argument('idf_output', nargs='?', type=argparse.FileType('w'), default='corp_idf_brown.csv',
                    help='where to write the csv idf output')

args = parser.parse_args()

# TODO: remove numbers (we have words like 2146 in corpus)

# Set up translation table for use with string.translate(translator)
translator = str.maketrans('', '', punctuation)

words = brown.words()

corp_words = []
for w in words:
    word = w.lower().translate(translator).strip()

    if len(word) > 1:
        corp_words.append(word)
        # print("w = {}, len(w) = {}".format(word, len(word)))

# Vectorize by frequency

counts = Counter(corp_words)

# Write our frequency vector result to csv
# Also calculate
# Credit to https://stackoverflow.com/a/19739263/8829491 for csv.write one-liner

with args.freq_output as csv:
    csv.write("len(corpus),{}\n".format(len(corp_words)))
    [csv.write('{0},{1}\n'.format(key, value)) for key, value in counts.items()]




# TODO: improve performance so that we can generate corpus quickly
# for each file: create dictionary
# for word, dictionary[word] = True
# append to list
docs = brown.fileids()
result = []
doc_dicts = []

for f in docs:
    cur_dict = {}
    doc = brown.words(f)
    doc = [w.lower().translate(translator).strip() for w in doc]

    for w in doc:
        cur_dict[w] = True
    doc_dicts.append(cur_dict
                     )
# Delete following after new implementation
'''
for (key, value) in counts.items():
	print(w)
	w  = key
	count = 0
	for f in docs:
		doc = brown.words(f)
		doc = [w.lower().translate(translator).strip() for w in doc ]
		if w in doc:
			count+=1

	# Done iterating, now write the IDF [log (total docs / # docs that contain term)]
	# TODO: log base 2 or 10 or e?
	print("{},{}".format(len(docs),count))
	IDF = log( len(docs) / count , 2)
	buf.append("{},{}".format(w, IDF))
'''

for (key, value) in counts.items():
    count = 0
    w = key
    for d in doc_dicts:
        count += d.get(w, 0)
    idf = log(len(docs) / count, 2)
    result.append((w, idf))

result = sorted(result, key=lambda tup: tup[1], reverse=True)
with args.idf_output as csv:
    [csv.write('{0},{1}\n'.format(key, value)) for key, value in result]

print("Finished writing to files")
