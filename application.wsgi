activate_this = '/home/pi/.virtualenvs/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os, sys, logging
logging.basicConfig(stream = sys.stderr)

PROJECT_DIR = '/srv/www/blueapp'
sys.path.append(PROJECT_DIR)

from mainapp import application as App

application = App()