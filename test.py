from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("rocks") == lemmatizer.lemmatize("rock"))