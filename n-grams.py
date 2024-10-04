import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

n= int(input("Enter value for n :- "))
text = input("Enter text :- ")

def generate_ngrams(text, n):
    global ngrams
    words = word_tokenize(text)
    ngrams = list(ngrams(words, n))
    return ngrams

print(generate_ngrams(text, n))