import nltk
from nltk.corpus import wordnet


class Dictionary(object):
	def lookup_word(self, word):
		return [synset.definition for synset in wordnet.synsets(word)]