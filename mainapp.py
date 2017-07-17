from flask import Flask
import os
working_dir = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(working_dir, 'templates')


application = Flask(__name__, template_folder=template_dir)
app = application

from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=3535, host='0.0.0.0')
