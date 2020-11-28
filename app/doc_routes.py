"""All the routes related to Doctor 
"""
from app import app 
from flask import render_template



@app.route('/doc/home')
def doc_home():
    return render_template('doc_templates/doc_home.html')
    #NOTE: add a new route and render function like this to display html pages.