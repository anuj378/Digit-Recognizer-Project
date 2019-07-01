# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 08:46:23 2019

@author: King23
"""
#importing libraries
from flask import Flask,render_template,request
import numpy as np
from PIL import Image
import base64
import io

# load json and create model
from keras.models import model_from_json

json_file = open('model_files/CNN_Predictor/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weights into new model
loaded_model.load_weights("model_files/CNN_Predictor/model.h5")
print("Loaded model from disk")

#make the predict function
loaded_model._make_predict_function()

#Instantiating the class Flask 
#app is the object that holds our project
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
    #Catching the data received 
    data=(request.form)
    #Slicing out only the required portion of the data (BASE64 string)
    #converting the clipped string into byte format as it is the supported format by the method decodebytes()
    data=base64.decodebytes(bytes((data['value'][22:]),'utf-8'))
    image = Image.open(io.BytesIO(data))
    #converting the image to greyscale
    image=image.convert('L')
    #resizing with smoothing (ANTIALIAS)
    image=image.resize((28,28),Image.ANTIALIAS)
    #converting the image to array
    image = np.asarray(image)
    #dividing each pixel intensity by 255 to apply MINMAX scaling
    image=image.astype('float32')/255
    #converting the image shape to that of the training data as it is what the model accepts
    image=image.reshape(1,28,28,1)
    #storing the index of the output array which has the greatest probabilistic value
    number=np.argmax(loaded_model.predict(image))
    #returning predicted number as a response
    if((type(number)!=None)):
        return ("PREDICTED NUMBER : "+str(number))
    else:
        return ("UNABLE TO PREDICT")

if __name__=='__main__':
    app.run()
