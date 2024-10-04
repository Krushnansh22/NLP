import nltk
prompt = input("Enter a sentence - ")

# Tokenization
tokens = nltk.word_tokenize(prompt)
print(f"Tokenized prompt :- \n{tokens}")

# # POS Tagging
# tags = nltk.pos_tag(tokens)
# print(f'POS tagging : \n{tags}\n')

# # named entities 
# print ('entities:-')
# entity = nltk.chunk.ne_chunk(tags)
# print(f"{entity}")

# # Parsing tree
# from nltk.corpus import treebank
# t = treebank.parsed_sents('wsj_0001.mrg')[1]
# t.draw()