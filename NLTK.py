import nltk
prompt = "Twinkle Twinkle Little Star how I wonder what you are. Up about the world so high like a diamond in the sky."
print(f'Prompt :- {prompt}')

# Tokenization
tokens = nltk.word_tokenize(prompt)
print(f"Tokenized prompt :- \n{tokens}")

# POS Tagging
tags = nltk.pos_tag(tokens)
print(f'POS tagging : \n{tags}')