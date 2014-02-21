
from subprocess import check_output, CalledProcessError
from flask import Flask, abort

app = Flask(__name__)


@app.route('/<bin>')
def hello(bin):
    try:
        return check_output(['which', bin])
    except CalledProcessError:
        abort(404)


@app.route('/gem/install/<gem>')
def gem_install(gem):
    try:
        return check_output(['gem', 'install', '--install-dir', '.', gem])
    except CalledProcessError as e:
        return e.message, 500
