from flask import Flask
import os

working_dir = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(working_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)
application = app
