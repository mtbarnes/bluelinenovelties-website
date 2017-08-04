activate_this = '/home/pi/.virtualenvs/blueline/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os, sys, logging
logging.basicConfig(stream = sys.stderr)

PROJECT_DIR = '/home/pi/blueline'
sys.path.append(PROJECT_DIR)

from manage import application as App

application = App
