import json
import gzip

def build_dictionary():
	dictionary = dict()
	from nltk.corpus import wordnet
	for synset in wordnet.all_synsets():
		for lemma in synset.lemmas:
			if lemma.name not in dictionary:
				dictionary[lemma.name] = [synset.definition]
			else:
				dictionary[lemma.name].append(synset.definition)

	json.dump(dictionary, gzip.open('dictionary.json.gzip', 'w'))
