import re
import os
import sys

class synonyms:
	def __init__(self):
		self.thes_csv = "Text_Analysis/thesaurus.csv"
		self.thesaurus = {}
		self.parse_thesaurus()

	def parse_thesaurus(self):

		with open(self.thes_csv) as csv:
			entries = csv.readlines()

		for line in entries:
			words = line.rstrip().split(",")
			word = words[0]
			for synonym in words[1:]:
				syn = synonym.lstrip()
				#print( "syn({}) = {}".format(word, syn) )
				if word in self.thesaurus:
					self.thesaurus[word].append(syn)
				else:
					self.thesaurus[word] = [syn]

	# Gets synonyms of multiple different meanings for the same given word
	def get_all_syns(self, word):
		# Search for word appended with any numbers
		poss = re.compile(word + "\d+")

		possibilities = [w for w in self.thesaurus if poss.search(w) != None]
		syns = []
		for w in possibilities:
			syns.append( self.get_syns(w) )
		return syns

	def get_syns(self, word):
		if word in self.thesaurus:
			return self.thesaurus[word]
		else:
			return -1

	def outp_syns(self, word):
		syns = self.get_syns(word)
		if syns == -1:
			print( "No synonyms for {}".format(word) )
		else:
			print("syns({})={}".format(word, syns))

	def output_test_strings(self):
		print("Querying test synonyms:")
		self.outp_syns("hate")
		self.outp_syns("love")
		self.outp_syns("greed")
		self.outp_syns("boy")
		print( self.get_all_syns("love") )
