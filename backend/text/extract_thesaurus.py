import re

# TODO: store meanings of word (as written in wordnet file) for better lookup

thesaurus_file = "princeton-core-wordnet.txt"
out_f = "thesaurus.csv"

# (?::+\] \[[a-z]+\] )(.*)
with open(thesaurus_file) as f:
	read_data = f.read()

thes_dict = {}
k = re.compile("[a-z] \[[a-z]*%")
# Synonym regex explained: Creates a non-capture group looking for something like
# "::] [write]", which precedes the synonyms. The second group, (.*), matches all the synonyms.
s = re.compile("(?::+\] \[[a-z]+\] )(.*)")

for elem in read_data.split("\n"):
	print("Searching element={}".format(elem))
	key_match = k.match(elem)
	syn_match = s.search(elem)

	word = ''
	synonyms = ''

	if (key_match):
		g = key_match.group()
		word = g[3:-1]
		print("Matched on key (word)={}".format(word))
	else:
		print("Did not match to a key")

	if (syn_match):
		synonyms = syn_match.group(1).rstrip()
		print("synonym={}".format(synonyms))
	else:
		print("No synonym match")

	if key_match and syn_match:
		# If we already have an entry, append a unique number to the key
		if word in thes_dict:
			append = 2
			while word in thes_dict:
				if word[-1] == str(append-1):
					word = word[:-1]
				word += str(append)
				append+=1

		thes_dict[word] = synonyms

# Write thes_dict to file
# Credit to https://stackoverflow.com/a/19739263/8829491
with open(out_f, 'w') as csv:
	[csv.write('{0},{1}\n'.format(key, value)) for key, value in thes_dict.items()]
