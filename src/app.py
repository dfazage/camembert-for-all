# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:19:09 2019

@author: fmustaffa
"""

#app for serving camembert model as an API service

from flask import Flask, request, jsonify
import os
import socket
import tempfile
from pathlib import Path
import numpy as np
from transformers import CamembertModel, CamembertTokenizer

model = CamembertModel.from_pretrained('/camembert-model')
token = CamembertModel.from_pretrained('/camembert-model')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def root():
    print("/")
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("LASER", "world"), hostname=socket.gethostname())


@app.route("/embedding")
def embedding():
    