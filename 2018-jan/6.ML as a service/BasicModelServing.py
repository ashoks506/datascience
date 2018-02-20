# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:56:55 2017

@author: asatharla
"""

from flask import Flask, jsonify, request
from sklearn.externals import joblib
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
@app.route('/', methods=['GET'])
def getmethod():
    return "Hello This is accessing from client get method"
@app.route('/home',methods=['POST'])
def home():
    return "This is Post Method name Home"
@app.route('/both',methods=['POST','GET'])
def bothmethods():
    return "This is get and Post Method name Home"

MODEL_DIR = 'D:/Projects/datasets'
MODEL_FILE = 'decision-tree-v1.pkl'
if __name__ == '__main__':
     os.chdir(MODEL_DIR)
     dt_estimator = joblib.load(MODEL_FILE)
     app.run(port=6696)