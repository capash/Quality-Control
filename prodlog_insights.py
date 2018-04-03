

import csv
from pandas.io.json import json_normalize
import flatten_json
import pandas as pd
from pandas import read_csv
import numpy as np
import ast


# Converting .tsv to .csv - Sales File
with open('C:\Blank\R\RockPaperScissors\Production_logs.tsv', 'r', encoding='utf-8', newline='') as fin, \
     open('C:\Blank\R\RockPaperScissors\Production_logs.csv', 'w', encoding='utf-8', newline='') as fout: # f output
     
     reader = csv.reader(fin, dialect='excel-tab')
     writer = csv.writer(fout, delimiter='|')     # here without a dialect, explicitly
     
     # Loop through the rows returned by the reader, and write them to the writer.
     for row in reader:
         writer.writerow(row)

# loading csv data to pandas dataframe
df = pd.read_csv('C:\Blank\R\RockPaperScissors\Production_logs.csv',delimiter='|', index_col=None)
df.columns = ['produnitId', 'batchId', 'item_produced', 'items_discarded']
df.to_csv('C:\Blank\R\RockPaperScissors\Production_logs_new.csv')


# Formatting the list type columns

def only_dict(d):
    '''
    Convert json string representation of dictionary to a python dict
    '''
    return ast.literal_eval(d)

def list_of_dicts(ld):
    '''
    Create a mapping of the tuples formed after 
    converting json strings of list to a python list   
    '''
    return dict([(list(d.values())[1], list(d.values())[0]) for d in ast.literal_eval(ld)])

A = json_normalize(df['item_produced'].apply(only_dict).tolist()).add_prefix('item_produced.')
B = json_normalize(df['items_discarded'].apply(only_dict).tolist()).add_prefix('items_discarded.')
df = df[['produnitId', 'batchId']].join([A, B])

# Write the final file to csv
df.to_csv('C:\Blank\R\RockPaperScissors\Production_logs_final.csv', sep='|', encoding='utf-8')

