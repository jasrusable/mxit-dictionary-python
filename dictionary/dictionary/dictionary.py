import nltk
from nltk.corpus import wordnet
import os

class Dictionary(object):
	def __init__(self):
		if 'CI' not in os.environ:
			try:
				wordnet.synsets('word')
			except:
				nltk.download('wordnet')
		else:
			print ("Dictionary running in CI mode.")

	def lookup_word(self, word):
		return [synset.definition for synset in wordnet.synsets(word)]
