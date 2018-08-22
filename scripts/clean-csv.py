
import csv
import re

import numpy as np
import pandas as pd
import itertools as it
import argparse as ap

# Parse arguments
parser = ap.ArgumentParser()
parser.add_argument('-i', '--input_csv', help='path to csv to be cleaned')
parser.add_argument('-o', '--output_csv', help='path to csv to be created')
args = parser.parse_args()

input_csv = args.input_csv
output_csv = args.output_csv

with open(input_csv, 'rt') as f:
    data = f.readlines()

# Remove unnecessasary double quotes
new_rows = list()
for row in data:
    matches = list(re.finditer(r'"', row))
    if len(matches) > 4:
        indices = [match.start() for match in matches[1:-3]]
        indices = [-1] + indices + [len(row)]
        new_row = ''
        for i in range(len(indices)-1):
            new_row = new_row + row[indices[i]+1:indices[i+1]]
        new_rows.append(new_row)
    else:
        new_rows.append(row)

# Output temporary csv
with open(output_csv, 'wt') as f:
    f.writelines(new_rows)
    
def repair_tweet(tweet):
    tweet = re.sub('# ', '#', tweet)
    tweet = re.sub('@ ', '@', tweet)
    return tweet

# Combine @'s and #'s with respective text
df = pd.read_csv(output_csv, delimiter=';')
df = df.drop(['geo', 'mentions', 'hashtags', 'id', 'permalink'], axis='columns')
df.columns = ['user', 'timestamp', 'retweets', 'likes', 'text']
df['text'] = df['text'].apply(repair_tweet)

# Save output csv
df.to_csv(output_csv, index=False)