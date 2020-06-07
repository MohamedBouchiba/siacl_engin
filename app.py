import requests
import json
from flask import Flask, render_template, jsonify
from pprint import pprint
from datetime import datetime
from flask import Flask, jsonify, request, send_from_directory
from elasticsearch import Elasticsearch

app = Flask(__name__ , static_url_path='')
es = Elasticsearch()

@app.route('/resultat', methods=['POST', 'GET'])
def resultat():

    # keyword = request.form['keyword']
    if request.method == 'POST':
        result = request.form.getlist('search_input')[0]
    else:
        result = ""
    body = {
        "query": {
            "multi_match": {
                "query": result,
                "fields": ["doc"]
            }
        }
    }

    my_json = es.search(index=['avis_siacl'], body=body, size=20, from_=0)

    hits_array = my_json["hits"]["hits"]
    list_fields = []
    for elem in hits_array:
        list_fields.append(elem)

    return render_template('index.html', resultat=list_fields)


@app.route('/')
def index():
    return render_template('search.html')
