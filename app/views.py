from app import app
from flask import render_template, jsonify
import urllib.request
import json

@app.route('/getloc')
def getloc():
	req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
	response = urllib.request.urlopen(req)
	obj = json.loads(response.read().decode('utf-8'))
	lat = obj['iss_position']['latitude']
	lng = obj['iss_position']['longitude']

	return jsonify(lat=lat, lng=lng)

@app.route('/')
def index():

	return render_template('index.html')