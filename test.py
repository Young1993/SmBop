from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("rocks") == lemmatizer.lemmatize("rock"))

import spacy

# import sqlite3
# from pathlib import Path
#
# sqlite_path = Path('dataset/database') / 'academic' / "academic.sqlite"
# source: sqlite3.Connection
# with sqlite3.connect(sqlite_path) as source:
#     dest = sqlite3.connect(":memory:")
#     dest.row_factory = sqlite3.Row
#     source.backup(dest)
#     print(source)
#
# sql = "SELECT * from author"
# db_conn= dest
# cursor = db_conn.cursor()
# cursor.execute(sql)
# p_res = cursor.fetchall()