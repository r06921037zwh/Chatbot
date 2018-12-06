# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 16:34:45 2018

@author: zhewei
"""
import numpy as np
import tensorflow as tf 
import re
import time

# read in dataset 
lines = open('movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
conversations = open('movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')

# creates a id2line map to record lines and its corresponding id
id2line = {}
for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5:
        id2line[_line[0]] = _line[4] 
        
# create a list of all conversations
conversation_ids = []
for conversation in conversations[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'", "").replace(",", "")
    conversation_ids.append(_conversation.split(" "))

# make question-answer pairs
questions, answers = [], []
for conversation in conversation_ids:
    for i in range(len(conversation) - 1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])
        
# first clean the texts