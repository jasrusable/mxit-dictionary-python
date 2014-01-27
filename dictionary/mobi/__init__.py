from flask import Blueprint, request
from dictionary import dictionary_instance

blueprint = Blueprint('mobi', __name__)

@blueprint.route('/')
def index():
	return 'Enter a word to search for:'

@blueprint.route('/lookup_word')
def lookup_word():
	word = request.args.get('word')
	definitions = dictionary_instance.lookup_word(word)
	return ''.join(definitions)
