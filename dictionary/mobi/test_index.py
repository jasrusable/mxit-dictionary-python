from flask.ext.testing import TestCase, Twill
from dictionary import app
from dictionary.mobi import resources as r
from bs4 import BeautifulSoup


class TestIndex(TestCase):
	"""Test homepage.
	"""
	def create_app(self):
		app.config['TESTING'] = True
		return app

	def test_welcome_message_present(self):
		with Twill(self.app, port=5000) as t:
			t.browser.go(t.url('/mobi/'))
			soup = BeautifulSoup(t.browser.get_html())
			self.assertEqual(unicode(soup.p.string).strip(),
				r.index.welcome_message_text)
