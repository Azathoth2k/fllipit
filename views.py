from flask import render_template
from fllipit import APP

@APP.route('/')
def index():
    return render_template('index.html', title=APP.config['EVENT_NAME'])