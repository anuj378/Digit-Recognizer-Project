# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 08:46:23 2019

@author: King23
"""

from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import PIL as pil
#import keras


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
@app.route('/predict',methods=['POST'])
def predict():
	data=request.form
	print("IMAGE DATA----->",data['value'])
	#print("DATA RECEVIED!",value.getlist('image_array'))
	#print("THE TYPE IS :",type(value['image_array']))
	
	if(data):
		return ("DATA RECEIVED!")
	else:
		return ("NO DATA RECEIVED")



if __name__=='__main__':
	app.run(debug=True)
