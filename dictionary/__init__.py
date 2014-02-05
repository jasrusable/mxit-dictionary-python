from flask import Flask, redirect, url_for
from dictionary import Dictionary

app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('mobi.index'))

dictionary_instance = Dictionary()

import mobi
app.register_blueprint(mobi.blueprint, url_prefix='/mobi')