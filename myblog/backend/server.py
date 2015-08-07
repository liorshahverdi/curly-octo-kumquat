from flask import Flask, request, render_template
import pickle
import json
from datetime import datetime
app = Flask(__name__)

@app.route("/",methods=["GET"])
def viewer():
    return render_template("index.html",data=pickle.load(open("data","rb")))

@app.route("/get_data",methods=["GET","POST"])
def get_data():
    return json.dumps(pickle.load(open("data","rb")))

@app.route("/send_data/<datum>",methods=["GET","POST"])
def send_data(datum):
    datum = json.loads(datum)
    datum["date"] = str(datetime.now())
    data = pickle.load(open("data","rb"))
    data.append(datum)
    pickle.dump(data,open("data","wb"))
    return "successfully added " + str(datum)

app.run(host='0.0.0.0', port=5010, debug=True)
