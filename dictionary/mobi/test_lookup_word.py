from flask.ext.testing import TestCase, Twill
from flask import url_for
from dictionary import app
from mock import Mock, patch
from bs4 import BeautifulSoup


class TestLookupWord(TestCase):
	"""Test Lookup Word.
	"""
	def create_app(self):
		app.config['TESTING'] = True
		return app

	def test_calls_lookup_word(self):
		def check(word, defs):
			with patch('dictionary.mobi.dictionary_instance') as mock_dictionary:
				mock_dictionary.lookup_word = Mock(return_value=defs)
				with Twill(self.app, port=5000) as t:
					t.browser.go(t.url('/mobi/lookup_word?word=%s' % word))
					mock_dictionary.lookup_word.assert_called_with(word)
		for word, defs in [("", []), ("sdf", ["hello"])]:
			check(word, defs)

	def test_lookup_word_results(self):
		with Twill(self.app, port=5000) as t:
			word = 'hello'
			test_definitions = ['a greeting', 'jasonii']
			with patch('dictionary.mobi.dictionary_instance') as mock_dictionary:
				mock_dictionary.lookup_word = Mock(return_value=test_definitions)
				t.browser.go(t.url(url_for('mobi.lookup_word', word=word)))
				soup = BeautifulSoup(t.browser.get_html())
				results = [unicode(result_element.string.strip()) for result_element in soup.ul.find_all('li')]
				self.assertEquals(results, test_definitions )
