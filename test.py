# read the metric json
import os
import json
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_json(filename):
    f = open(filename)
    content = f.read()
    return json.loads(content)

def report_statistics(type='validation', name='spider'):
    df_1 = pd.read_csv('./experiments/beady-harlequin-horse.csv')
    df_2 = pd.read_csv('./experiments/goopy-viridian-lion.csv')
    df_3 = pd.read_csv('./experiments/greasy-persimmon-hippopotamus.csv')
    # print(df.info())

    df_1 = df_1.sort_values('epoch')
    x = np.array(df_1.epoch.to_list())
    y = np.array(df_1[f'{type}_{name}'].to_list())
    plt.plot(x, y, label='schema + DB value')

    df_2 = df_2.sort_values('epoch')
    x2 = np.array(df_2.epoch.to_list()[:93])
    y2 = np.array(df_2[f'{type}_{name}'].to_list()[:93])
    plt.plot(x2, y2, label='schema')

    df_3 = df_3.sort_values('epoch')
    x3 = np.array(df_3.epoch.to_list()[:93])
    y3 = np.array(df_3[f'{type}_{name}'].to_list()[:93])
    plt.plot(x3, y3, label='SmBop')

    plt.xlabel('epoch')
    plt.ylabel('acc')
    plt.title(type + " " + name)
    plt.legend()
    plt.show()


report_statistics('training','loss')

def report_csv():
    base = os.listdir('./experiments')
    for file in base:
        # print(file)

        df = {
            "validation_final_beam_acc": [],
            "validation_spider": [],
            "training_loss":[],
            "epoch": [],
            "validation_reranker": [],
            "validation_leafs_acc": []
        }

        experiment = os.listdir('./experiments/' + file)
        for block in experiment:
            if block.find('metrics_epoch_') > -1:
                print(block)
                metric = read_json(Path('experiments') / file / block)
                df['validation_final_beam_acc'].append(metric['validation_final_beam_acc'])
                df['validation_spider'].append(metric['validation_spider'])
                df['training_loss'].append(metric['training_loss'])
                df['epoch'].append(metric['epoch'])
                df['validation_reranker'].append(metric['validation_reranker'])
                df['validation_leafs_acc'].append(metric['validation_leafs_acc'])

        df = pd.DataFrame(df)
        df.to_csv(file + '.csv', index=False)

'''
nltk stem lemmatizer
'''

# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize("rocks") == lemmatizer.lemmatize("rock"))

'''
Spacy word similarity
'''

# import spacy
# nlp = spacy.load('en_core_web_md')
#
# token_1 = nlp('cat')
# token_2 = nlp('dog')
# print("Similarity:", token_1.similarity(token_2))

'''
sqlite
'''
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
