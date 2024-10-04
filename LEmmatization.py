from nltk.stem import WordNetLemmatizer
import nltk
l = WordNetLemmatizer()
sentence = "Summator performs summations into the multiplication"
tokens = nltk.word_tokenize(sentence)

for w in tokens:
    print(f'{w} -> {l.lemmatize(w)}')