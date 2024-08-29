from crypt import methods
import flask
from flask import request
import json
from textwrap import indent
from random import randint, randrange

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    #return 'the home page stuff...'
    ret = {'success': True, 'message': "This is the home page"}
    return json.dumps(ret), 200, {'Content-type': 'application/json'}


json_file = json.load(open('dadjokes.json', 'r', encoding='utf-8'))
IDList=[]
List = []
    
f = open('dadjokes.json')
data = json.load(f)

for i in data:
    joke = i
    ID = i['id']
    List.append(joke)
    IDList.append(ID)

'''
def getName(self):
    json_file = json.load(open('dadjokes.json', 'r', encoding='utf-8'))
    nameList =[]

    f = open('dadjokes.json')
    data = json.load(f)

    for i in data:
        name = i
        nameList.append(name)

    num = random.randint(0, len(nameList))
    return nameList[num]

def getJoke(self):
    json_file = json.load(open('dadjokes.json', 'r', encoding='utf-8'))
    jokeList = []

    f = open('dadjokes.json')
    data = json.load(f)

    for i in data:
        joke = i
        jokeList.append(joke)

    num = random.randint(0, len(jokeList))
    return jokeList[num]'''

@app.route('/random', methods=['GET'])
def random():
    ans = List[randrange(len(IDList)-10)+randrange(9)]
    return json.dumps(ans), 200, {'Content-type': 'application/json'}


@app.route('/joke', methods=['GET'])
def joke():
    if 'id' in request.args:
        str = request.args['id']
        if str in IDList:
            numm = IDList.index(str)
            ans = List[numm]
            return json.dumps(ans), 200, {'Content-Type': 'application/json'}
        else: 
            return 'nope', 400
    else: 
        return 'nope', 400


@app.errorhandler(404)
def err_404(e):
    return "Couldn't find page", 404


app.run(host='127.0.0.1', port=3001)
