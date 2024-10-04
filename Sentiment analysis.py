from textblob import TextBlob

def classify_sentence(sentence):
    blob = TextBlob(sentence)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity * 5  # Scale to 0-5
    
    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return sentiment, polarity, subjectivity

sentences = [
    "I love this product!",
    "This is the worst experience I've ever had.",
    "It's okay, nothing special.",
]

for sentence in sentences:
    sentiment, polarity, subjectivity = classify_sentence(sentence)
    print(f"Sentence: '{sentence}'")
    print(f"Sentiment: {sentiment}, Polarity: {polarity:.3f}, Subjectivity: {subjectivity:.2f}\n")