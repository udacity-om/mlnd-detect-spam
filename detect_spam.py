import pandas as pd
# Dataset from - https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
df = pd.read_table('smsspamcollection/SMSSpamCollection',
                   sep='\t', 
                   header=None, 
                   names=['label', 'sms_message'])

# Output printing out first 5 columns
# print(df.head())

df['label'] = df.label.map({'ham':0, 'spam':1})
print(df.shape) # returns (rows, columns)
print(df.head)
