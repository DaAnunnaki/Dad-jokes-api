import flask
from flask import request, abort 
import json 
import random 
#pip install flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    ret = {'success': True, 'message': "This is the home page"}
    return json.dumps(ret), 200, {'Content-type': 'application/json'}

@app.route('/add', methods=['GET'])
def add_numbers():
    if 'a' in request.args and 'b' in request.args:
        ans = {'answer': int(request.args['a']) + int(request.args['b'])}
        return json.dumps(ans), 200, {'Content-Type': 'application/json'}
    else: 
        return 'nope', 400

@app.errorhandler(404)
def err_404(e):
    return "Couldn't find page", 404

app.run(host='127.0.0.1', port=3001)