from flask import Flask, render_template, request, url_for
from response_processor import response_processor
import requests
import json

app = Flask(__name__)

login_token = ""

@app.route("/")
def search():
    return render_template("search.html",login_token=login_token)

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

    #comment out the sending request to style and modify result page
    #response = requests.request('GET', url, headers=headers).json()
    
    with open("test.json","r") as json_file:
        response = json.load(json_file)

    if response["results"] == []:
        return "no results"
    else:
        #response=json.dumps(response)
        # results = response_processor(response)
        return render_template("result.html", response = response,login_token=login_token)

@app.route("/sign_in")
def sign_in():
    
    return render_template("signin.html")

@app.route("/sign_up")
def sign_up():
    
    return render_template("signup.html")

@app.route("/summary")
def summary():
    return ""

@app.route("/account")
def account():
    return ""

if __name__ == "__main__":
    app.run(debug = True)