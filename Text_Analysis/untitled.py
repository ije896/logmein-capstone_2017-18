# Reads in from csv file for use in calculating tf_idf

class tf_idf:
	def __init__(self):
		self.freqs_csv = "Text_Analysis/corp_freqs_brown.csv"
		self.len_corp = 0
		self.freqs = {}
		self.parse_freqs()

	def parse_freqs(self):
		with open(self.freqs_csv, 'r') as csv:
			first = csv.readline()
			rest = csv.readlines()

			(sentinel, length) = first.rstrip().split(',')
			assert(sentinel == "len(corpus)")
			self.len_corp = length

			for line in rest:
				(word, f) = line.strip().split('')
				self.freqs[word] = f

	def analyze_text(text):
		


