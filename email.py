import nltk
from nltk.tokenize import RegexpTokenizer

# Sample email addresses
emails = ["alice@example.com", "bob123@gmail.com", "carol.doe@domain.org"]

# Regular expression to match the username part of an email
username_pattern = r'^[\w.-]+'

# Create a regular expression tokenizer
tokenizer = RegexpTokenizer(username_pattern)

# Extract and print usernames
usernames = [tokenizer.tokenize(email)[0] for email in emails]
print("Usernames:", usernames)
