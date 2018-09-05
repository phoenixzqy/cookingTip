#-*- coding: utf-8 -*-
import json


db_path = "static/db.json"
def init():
    global config
    with open('static/config.json', 'r') as f:
        config = json.load(f)
    

