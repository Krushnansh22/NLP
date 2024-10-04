# import these modules
from nltk.stem import PorterStemmer
import os
ps = PorterStemmer()
while True:
    w = input("Enter Word to stemm :- ") 
    print(ps.stem(w))