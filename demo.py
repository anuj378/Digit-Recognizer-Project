# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 08:46:23 2019

@author: King23
"""

from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")
@app.route('/links')
def showLinks():
	return render_template("links.html")
@app.route('/devs')
def showDevs():
	return render_template("devs.html")



if __name__=='__main__':
	app.run(debug=True)
