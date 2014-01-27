from flask import Flask
from dictionary import Dictionary

app = Flask(__name__)

dictionary_instance = Dictionary()

import mobi
app.register_blueprint(mobi.blueprint, url_prefix='/mobi')