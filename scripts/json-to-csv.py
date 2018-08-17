import json
import pandas as pd

with open('save-the-expanse.json') as f:
    tweets = json.load(f)

tweets_df = pd.DataFrame(tweets)
tweets_df = tweets_df.drop(['html', 'id', 'url'], axis='columns')
tweets_df['timestamp'] = pd.to_datetime(tweets_df['timestamp'])
tweets_df.to_csv('save-the-expanse.csv', index=False)