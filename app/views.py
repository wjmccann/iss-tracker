from app import app
from flask import render_template
import urllib.request
import json

@app.route('/')
def index():

	req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
	response = urllib.request.urlopen(req)
	obj = json.loads(response.read().decode('utf-8'))
	lat = obj['iss_position']['latitude']
	lng = obj['iss_position']['longitude']
	
	return render_template('index.html',
							lat=lat,
							lng=lng)