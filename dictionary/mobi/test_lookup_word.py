from flask.ext.testing import TestCase, Twill
from dictionary import app
from mock import Mock, patch


class TestLookupWord(TestCase):
	"""Test Lookup Word.
	"""
	def create_app(self):
		app.config['TESTING'] = True
		return app

	def test_definitions(self):
		def check(word, defs):
			with patch('dictionary.mobi.dictionary_instance') as mock_dictionary:
				mock_dictionary.lookup_word = Mock(return_value=defs)
				with Twill(self.app, port=5000) as t:
					t.browser.go(t.url('/mobi/lookup_word?word=%s' % word))
					mock_dictionary.lookup_word.assert_called_with(word)
		for word, defs in [("", []), ("sdf", ["hello"])]:
			check(word, defs)