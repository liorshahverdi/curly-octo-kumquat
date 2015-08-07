from flask import Flask, render_template, redirect, url_for, request
import requests
import json
from datetime import datetime
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
	if request.method=="POST":
		post = {}
                post["title"] = request.form.get("title")
		post["body"] = request.form.get("body")
		requests.post("http://localhost:5010/send_data/"+json.dumps(post))
	return render_template('add.html')

@app.route('/historical_list', methods=['GET', 'POST'])
def historical_list():
        r=requests.get("http://localhost:5010/get_data")
        print r.text
	return render_template('historical_list.html',posts=json.loads(r.text))

app.run(host='0.0.0.0', port=5000, debug=True)
