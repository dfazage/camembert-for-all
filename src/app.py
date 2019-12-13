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
import torch
from transformers import CamembertModel, CamembertTokenizer


#preload init models from docker
model = CamembertModel.from_pretrained('/camembert-model')
tokenizer = CamembertTokenizer.from_pretrained('/camembert-model')

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
    
    #parameters
    content = request.args.get('q')
    
    # encode() automatically adds the classification token <s>
    token_ids = tokenizer.encode(content)
    tokens = [tokenizer._convert_id_to_token(idx) for idx in token_ids]

    # unsqueeze token_ids because batch_size=1
    token_ids = torch.tensor(token_ids).unsqueeze(0)

    # forward method returns a tuple (we only want the logits)
    # squeeze() because batch_size=1
    output = model(token_ids)[0].squeeze()
    # only grab output of CLS token (<s>), which is the first token
    cls_out = output[0]
    
    #json body return
    body = {'content': content, 'embedding':cls_out.data.numpy().tolist()}
    
    return(jsonify(body))
    
if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0', use_reloader=False)