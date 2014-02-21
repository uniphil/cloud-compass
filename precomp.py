
from subprocess import check_output, CalledProcessError
from flask import Flask, abort

app = Flask(__name__)
app.debug = True


@app.route('/<bin>')
def hello(bin):
    try:
        return check_output(['which', bin])
    except CalledProcessError:
        abort(404)


@app.route('/ls/')
@app.route('/ls/<path:dir>')
def ls(dir='.'):
    try:
        return check_output(['ls', dir])
    except CalledProcessError as e:
        return str(e), 500


@app.route('/bash/<path:cmd>')
def bash(cmd):
    try:
        return check_output(cmd.split())
    except CalledProcessError as e:
        return str(e), 500


@app.route('/gem/install/<gem>')
def gem_install(gem):
    try:
        return check_output(['gem', 'install', '--install-dir', '.', gem])
    except CalledProcessError as e:
        return str(e), 500
