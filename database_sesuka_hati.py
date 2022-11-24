# -*- coding: utf-8 -*-
"""Database sesuka hati

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jUD6V-kzuQtmRpu19hDHxvkZ9wINMrT-
"""

from sklearn import tree
# Database: Gerbang logika AND
# x = Data, y = Target
x = [[0,0], [0,1], [1,0], [1,1], [1,2], [1,3], [2,1], [2,3], [2,5], [2,8]]
y = [0,0,0,1,2,1,1,3,5,6]

# Training and Classify. 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

# Prediksi
print ("Logika AND Metode Desicion Tree")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]])) 
print ("0 1 = ", clf.predict([[0,1]])) 
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))
print ("1 2 = ", clf.predict([[1,2]]))
print ("1 3 = ", clf.predict([[1,3]]))
print ("2 1 = ", clf.predict([[2,1]]))
print ("2 3 = ", clf.predict([[2,3]]))
print ("2 5 = ", clf.predict([[2,5]]))
print ("2 8 = ", clf.predict([[2,8]]))