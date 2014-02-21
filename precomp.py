
from subprocess import check_output, CalledProcessError
from flask import Flask, abort

app = Flask(__name__)


@app.route('/<bin>')
def hello(bin):
    try:
        return check_output(['which', bin])
    except CalledProcessError:
        abort(404)
