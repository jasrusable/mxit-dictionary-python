from flask import Blueprint, request, render_template
from dictionary import dictionary_instance
from dictionary.mobi import resources as r

blueprint = Blueprint('mobi', __name__, template_folder='templates')

@blueprint.route('/')
def index():
	res = render_template('index.html',
		welcome_message_text=r.index.welcome_message_text,
	)
	return res

@blueprint.route('/lookup_word')
def lookup_word():
	word = request.args.get('word')
	definitions = dictionary_instance.lookup_word(word)
	return render_template('lookup_word.html', defined_word=word, definitions=definitions, lookup_new_word_text=r.lookup_word.lookup_new_word_text)