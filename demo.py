# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 08:46:23 2019

@author: King23
"""

from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import PIL as pil
from PIL import Image
import keras
import matplotlib.pyplot as plt
import base64
import io
#importing model
# load json and create model
from keras.models import model_from_json

json_file = open('model_files/CNN_Predictor/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

loaded_model = model_from_json(loaded_model_json)
loaded_model._make_predict_function()

# load weights into new model

loaded_model.load_weights("model_files/CNN_Predictor/model.h5")
print("Loaded model from disk")

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
    data=dict(request.form)
    data=base64.decodebytes(bytes((data['value'][22:]),'utf-8'))
    #image =Image.frombytes('L',(28,28),data)
    image = Image.open(io.BytesIO(data))
    image=image.convert('L')
    image.thumbnail((28,28))
    image=np.array(image)
    plt.imshow(image)
    image=image/255
    image=image.reshape(1,28,28,1)
    number=np.argmax(loaded_model.predict(image))
    if(number):
        return ("PREDICTED NUMBER : "+str(number))
    else:
        return ("UNABLE TO PREDICT")



if __name__=='__main__':
    app.run()
