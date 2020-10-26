from flask import Flask, render_template, request, url_for
from response_processor import response_processor
import requests
import json

app = Flask(__name__)

@app.route("/")
def search():
    return render_template("search.html")

@app.route("/result", methods=["POST"])
def result():
    keyword = str(request.form.get("searchkey"))
    newkeyword = ''
    for i in keyword:
        if i == ' ':
            n = '%20'
        elif i == '@':
            n = '%40'
        elif i == '#':
            n = '%23'
        elif i == '$':
            n = '%24'
        elif i == '%':
            n = '%25'
        elif i == '^':
            n = '%5'+'E'
        else:
            n = i
        newkeyword += n 
    url = 'https://listen-api.listennotes.com/api/v2/search?q=' + newkeyword +'&sort_by_date=0&type=episode&offset=0&len_min=10&len_max=30&genre_ids=68%2C82&published_before=1580172454000&published_after=0&only_in=title%2Cdescription&language=English&safe_mode=0'
    headers = {
        'X-ListenAPI-Key': 'ce8e7ce414414764be7159d0aeecdb16',
    }
    response = json.dumps(requests.request('GET', url, headers=headers).json())
    results = response_processor(response)
    return render_template("result.html", results = results)

@app.route("/summary")
def summary():
    return ""

app.run(debug = True)