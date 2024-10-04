#bigram language model
import nltk
from nltk.util import bigrams
text = input("Enter sentence:-")
tokens = nltk.word_tokenize(text)
def create_bigrams(text):
    global bigrams
    bigrams = list(bigrams(tokens))
    return bigrams
print(create_bigrams(text))


#trigram
from nltk.util import trigrams
def create_trigrams(text):
    global trigrams
    trigrams = list(trigrams(tokens))
    return trigrams

print(create_trigrams(text))