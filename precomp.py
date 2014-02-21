
from subprocess import check_output, CalledProcessError
from flask import Flask, abort

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello():
    return ("welcome to precomp. you'll want to set up your own:"
            '<a href="https://github.com/uniphil/cloud-compass">source repo</a>')


@app.route('/sass', methods=['POST'])
def sassy():
    # accept the posted tarball
    # save it somewhere
    # compile it
    # send the compiled file back
    return ''
