import nltk
from nltk.tokenize import word_tokenize

# Sample text
text = "Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics."

# Tokenize the text
tokens = word_tokenize(text)

# Write tokens to a file
# with open('tokens.txt', 'w') as file:
#     for token in tokens:
#         file.write(token + '\n')

print("Tokens have been written to tokens.txt")
with open('file.txt', 'r') as file:
    
    print(file.readline())