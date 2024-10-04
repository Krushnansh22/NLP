def remove(text):
    tokens = nltk.word_tokenize(text)
    filterd = ""
    for word in tokens :
        if word.lower() not in stops: filterd+=word+" "
    return filterd