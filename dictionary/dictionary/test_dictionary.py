import unittest
from dictionary import Dictionary
from mock import Mock, patch

class TestDictionary(unittest.TestCase):
	def setUp(self):
		self.dictionary = Dictionary()
