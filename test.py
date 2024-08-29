from crypt import methods
import flask
from flask import request
import json
import random
from textwrap import indent
import random

json_file = json.load(open('dadjokes.json', 'r', encoding='utf-8'))
IDList=[]
nameList =[]
jokeList = []

f = open('dadjokes.json')
data = json.load(f)
#print(data)

for i in data:
    ID = i
    IDD = i['id']
    name = i['name']
    joke = i['joke']
    IDList.append(ID)
    nameList.append(IDD)
    jokeList.append(joke)

num = random.randint(0, len(IDList))
numm = nameList.index("2eac2186")
print(IDList[numm])