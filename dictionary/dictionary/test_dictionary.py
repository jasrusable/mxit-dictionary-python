import unittest
from dictionary import Dictionary
from mock import Mock, patch

class TestDictionary(unittest.TestCase):
	def setUp(self):
		self.dictionary = Dictionary()

	def test_lookup_word(self):
		with patch('dictionary.dictionary.dictionary.wordnet') as wordnet:
			mock_synsets = list()
			definitions = ['hello', 'bye']
			for definition in definitions:
				mock_synset = Mock()
				mock_synset.definition = definition
				mock_synsets.append(mock_synset)
			wordnet.synsets = Mock(return_value=mock_synsets)	
			test_word = 'hello'
			results = self.dictionary.lookup_word(test_word)
			self.assertIsInstance(results, list)
			for result in results:
				self.assertIsInstance(result, basestring)
			self.assertEqual(results, definitions)
			wordnet.synsets.assert_called_with(test_word)

