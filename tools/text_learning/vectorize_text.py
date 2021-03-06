#!/usr/bin/python

import os
import pickle
import re
import sys
import string
from tools.parse_out_email_text import parseOutText
from sklearn.feature_extraction.text import TfidfVectorizer 
"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker



for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
    
        path = os.path.join('D:/Python/ud120-projects', path[:-1])
        email = open(path, "r")
        ### use parseOutText to extract the text from the opened email
        words=parseOutText(email)
        words=words.replace("sara","")
        words=words.replace("shackleton","")
        words=words.replace("chris","")
        words=words.replace("germani","")
        words=words.replace("sshacklensf","")
        words=words.replace("cgermannsf","")
        word_data.append(words)
        if(name=='sara'):
            from_data.append(0)
        else:
            from_data.append(1)

        ### use str.replace() to remove any instances of the words
        ### ["sara", "shackleton", "chris", "germani"]

        ### append the text to word_data

        ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris


        email.close()

pickle.dump(word_data, open("your_word_data_unix.pkl", "wb"))
pickle.dump(from_data, open("your_email_authors_unix.pkl", "wb"))

### in Part 4, do TfIdf vectorization here
vct=TfidfVectorizer(stop_words="english")
word_data=vct.fit_transform(word_data)
print(word_data)
print("-----------------------------------------------------")
print((vct.get_feature_names())[34597])
print ("emails processed")
from_sara.close()
from_chris.close()
