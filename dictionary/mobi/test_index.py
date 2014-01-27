from flask.ext.testing import TestCase, Twill
from dictionary import app


class TestIndex(TestCase):
	"""Test homepage.
	"""
	def create_app(self):
		app.config['TESTING'] = True
		return app

	def test_welcome_message_present(self):
		with Twill(self.app, port=5000) as t:
			t.browser.go(t.url('/mobi/'))
			self.assertEqual(t.browser.get_html(),
				"Enter a word to search for:")
