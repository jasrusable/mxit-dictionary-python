from flask.ext.testing import TestCase, Twill
from dictionary import app


class TestLookupWord(TestCase):
	"""Test Lookup Word.
	"""
	def create_app(self):
		app.config['TESTING'] = True
		return app

	def test_definitions(self):
		with Twill(self.app, port=5000) as t:
			t.browser.go(t.url('/mobi/lookup_word?word=dog'))
			pass