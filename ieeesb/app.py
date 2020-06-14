from flask import Flask, render_template, request , make_response, redirect, url_for
import os 
from datetime import datetime, timedelta
import datetime as dm

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
	pages = []
	ten_days_ago = dm.date.today() - timedelta(days = 10)
	for rule in app.url_map.iter_rules():
		if 'GET' in rule.methods and len(rule.arguments) == 0 and not rule.rule.startswith('/admin'):
			pages.append([ url_for('index', _external=True)  + rule.rule, ten_days_ago])
	sitemap_template = render_template('sitemap_template.xml', pages=pages)
	response = make_response(sitemap_template)
	response.headers["Content-Type"] = "application/xml"
	return response

