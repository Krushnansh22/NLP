import nltk
from nltk.corpus import stopwords
stops = stopwords.words('english')
def remove(text):

    tokens = nltk.word_tokenize(text)
    filterd = ""
    for word in tokens :
        if word.lower() not in stops: filterd+=word+" "
    return filterd

text = input("Enter sentence:-")
print("Filterd-",remove(text))
