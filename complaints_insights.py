

import csv
from pandas.io.json import json_normalize
import flatten_json
import pandas as pd
from pandas import read_csv
import numpy as np
import ast


# Converting .tsv to .csv - Sales File
with open('C:\Blank\R\RockPaperScissors\Complaints.tsv', 'r', encoding='utf-8', newline='') as fin, \
     open('C:\Blank\R\RockPaperScissors\Complaints.csv', 'w', encoding='utf-8', newline='') as fout: # f output
     
     reader = csv.reader(fin, dialect='excel-tab')
     writer = csv.writer(fout, delimiter='|')     # here without a dialect, explicitly
     
     # Loop through the rows returned by the reader, and write them to the writer.
     for row in reader:
         writer.writerow(row)

# loading csv data to pandas dataframe
df = pd.read_csv('C:\Blank\R\RockPaperScissors\Complaints.csv',delimiter='|', index_col=None)
df.columns = ['invoiceId', 'defectiveItem']
df.to_csv('C:\Blank\R\RockPaperScissors\Complaints_final.csv')




