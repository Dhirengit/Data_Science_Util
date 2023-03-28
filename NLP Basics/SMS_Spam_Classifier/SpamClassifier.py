# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

messages = pd.read_csv('C:/Users/Admin/Documents/Spider py/SMS_Spam_Classifier/SMSSpamCollection',
                       sep="\t", names=["label","messages"])

# Data Cleaning and Preprocessing
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
corpus = []

for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]',' ', messages['messages'][i])
    review = review.lower()
    review = review.split()
    
    review = [ps.stem(word) for word in review if word not in stopwords.words('english')]
    review = " ".join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=2500)
X = cv.fit_transform(corpus).toarray()

y = pd.get_dummies(messages['label'])
y = y.iloc[:,1].values


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=0)


from sklearn.naive_bayes import MultinomialNB
spam_dect_model = MultinomialNB().fit(X_train, y_train)

y_pred = spam_dect_model.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)

accuracy = accuracy_score(y_test, y_pred)



