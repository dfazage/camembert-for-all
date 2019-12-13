# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:44:18 2019

@author: fmustaffa
"""

#script for model laoding and saving (bypassing enedis proxy using local computer)
from transformers import CamembertModel, CamembertTokenizer

model = CamembertModel.from_pretrained('camembert-base')
tokenizer = CamembertModel.from_pretrained('camembert-base')

#save model
model.save_pretrained('/camembert-model')
tokenizer.save_pretrained('/camembert-model')