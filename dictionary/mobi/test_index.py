from flask.ext.testing import TestCase, Twill
from flask import url_for
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

	def test_lookup_form(self):
		with Twill(self.app, port=5000) as t:
			t.browser.go(t.url('/mobi'))
			soup = BeautifulSoup(t.browser.get_html())
			self.assertIsNotNone(soup.form)
			action = soup.form['action']
			self.assertIsNotNone(action)
			self.assertEqual(action, url_for('mobi.lookup_word')) 
			self.assertIsNotNone(soup.form.input)
			self.assertEqual(soup.form.input['name'], 'word')
			self.assertIsNotNone(soup.form.find('input', type='submit'))
