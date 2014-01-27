import unittest
from dictionary import Dictionary

class TestDictionary(unittest.TestCase):
	def setUp(self):
		self.dictionary = Dictionary()

	def test_lookup_word(self):
		results = self.dictionary.lookup_word('hello')
		self.assertIsInstance(results, list)
		for result in results:
			self.assertIsInstance(result, basestring)

