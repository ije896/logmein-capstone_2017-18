import string
# TODO: implement more than just flesch-kincaid (SMOG, etc)
# TODO: Consider using https://pypi.python.org/pypi/textstat/ - might be easier but writing the code ourselves = less dependencies

class Readability:

	# Flesh-Kincaid : 206.835 - 1.015(num_words/num_sents) - 84.6(num_sylls/num_words)
	@staticmethod
	def f_k(text):
		n_words = len( Readability.get_words(text) )
		n_sents =  Readability.get_num_sents(text)
		n_sylls =  Readability.get_num_sylls(text)

		return 206.835 - 1.015*(n_words/n_sents) - 84.6*(n_sylls/n_words)

	# Returns Flesh-Kincaid as a grade level string e.g. "5th grade", "college", etc
	@staticmethod
	def f_k_grade_level(text):
		# lte_grade_level: tup[0] is the value s.t. if it's fk >= tup[0] then tup[1] is the grade level
		# note we go from highest numbers down otherwise >= wouldn't work properly
		lte_grade_level = [(90, "5th grade"), (80, "6th grade"), (70, "7th grade"), (60, "8th and 9th grade"),
						   (50, "10th to 12th grade"), (30, "college"), (-10**6, "college graduate")] 

		fk = Readability.f_k(text)

		for gl in lte_grade_level:
			if fk >= gl[0]:
				return gl[1]

		return "fk_grade_level: something went wrong"


	@staticmethod
	def get_words(text):
		text = text.translate({ ord(c): '' for c in ".?!-:;="} ) # TODO: figure out if we've replaced enough (maybe use string.punctuation)
		words = text.split(' ')
		words = [w for w in words if len(w) > 0]
		return words

	@staticmethod
	def get_num_sents(text):
		text = text.replace("...", " ") # ellipses aren't a new sentence
		text = text.replace("?!", "!")  # ?! is just one sentence ending, not two
		text = text.replace("???", "?") # ??? is one sentence, not three

		text = text.translate({ ord(c): '.' for c in ".?!"} )
		split_punc = text.split('.')

		for s in split_punc:
			#print("s={}, len(s)={}".format(s, len(s)))
			if len(s) == 0:
				split_punc.remove(s)

		return len(split_punc)

	# Evil magic courtesy of https://codegolf.stackexchange.com/a/47326
	@staticmethod
	def sylls(w):
		remove_punct = str.maketrans('', '', string.punctuation)
		w = w.translate(remove_punct) # Remove punctuation just to be safe

		return len(''.join(" x"[c in"aeiouy"]for c in(w[:-1]if'e'==w[-1]else w)).split())

	# Get all syllables of text (ie sum sylls(word) for all words)
	@staticmethod
	def get_num_sylls(text):
		num_sylls = 0
		for w in Readability.get_words(text):
			num_sylls += Readability.sylls(w)
		return num_sylls

	@staticmethod
	def test_get_num_words():
		tests = [(6, "This is a really easy sentence."), (6, "Is this one harder? Probably not."), 
				 (2, "Exclamation point!"), (8, "the self-evident truth; blah blah blah 1992 blah")] # not sure how we should handle 1922 or hyphens

		for t in tests:
			print("\ntest_get_num_words: testing ({}), expect {}".format( t[1], t[0] ))
			assert( len(Readability.get_words(t[1])) == t[0] )
			print("PASS: test_get_num_words:  ({}) => {}".format( t[1], t[0] ))

	@staticmethod
	def test_get_num_sents():
		tests = [ (3, "Here's one. It's simple. The answer is 3."), (2, "Are you expecting question marks tho? I hope so."),
		   		  (2, "You won't get this one! Will you?"), (2, "Watch out... for... ellipses...they can be confusing. Seriously.") ]
		for t in tests:
			print("\ntest_get_num_sents: testing ({}), expect {}".format( t[1], t[0] ))
			print( t[1].split('.')  )
			assert( Readability.get_num_sents(t[1]) == t[0] )
			print("PASS: test_get_num_sents:  ({}) => {}".format( t[1], t[0] ))

	@staticmethod
	def output_tests():
		print("\n")
		# TODO: refactor this to print the raw fk score and the fk grade level as a tuple, and also output the string being tested (extract a helper function)
		print(Readability.f_k("This is a simple sentence that should not be too hard to read."))
		print(Readability.f_k("The cat sat on the mat."))
		print(Readability.f_k("We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness."))
		print(Readability.f_k_grade_level("This is a simple sentence that should not be too hard to read."))
		print(Readability.f_k_grade_level("The cat sat on the mat."))
		print(Readability.f_k_grade_level("We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness."))
		Readability.test_get_num_words()
		Readability.test_get_num_sents()
		

# TODO: Add testing for f_k readability (measure error from some reference standard)
# TODO: Add testing for f_k_grade level
	