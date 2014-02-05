import nltk
from nltk.corpus import wordnet
import json
import gzip
import os

class Dictionary(object):
	def __init__(self):
		f = gzip.open('dictionary.json.gzip', 'r')
		self.dictionary = json.load(f)

	def lookup_word(self, word):
		return self.dictionary.get(word.lower())
