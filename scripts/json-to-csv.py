import json
import pandas as pd
import argparse as ap
import os

parser = ap.ArgumentParser()
parser.add_argument('json_path', help='path to json file to be converted')
parser.add_argument('csv_path', help='path to csv file to be converted')

args = parser.parse_args()
json_path = args.json_path
csv_path = args.csv_path

csv_dirname = os.path.dirname(csv_path)
if not os.path.isdir(csv_dirname):
    os.makedirs(csv_dirname)

with open(json_path) as f:
    tweets = json.load(f)

tweets_df = pd.DataFrame(tweets)
tweets_df = tweets_df.drop(['html', 'id', 'url'], axis='columns')
tweets_df['timestamp'] = pd.to_datetime(tweets_df['timestamp'])
tweets_df.to_csv(csv_path, index=False)