import requests
import pandas as pd

SUBREDDIT = 'machinelearning'
LIMIT = 100
URL = f'https://www.reddit.com/r/{SUBREDDIT}/new.json?limit={LIMIT}'

HEADERS = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    data = response.json()
    posts = []
    for post in data['data']['children']:
        post_data = post['data']
        posts.append({
            'id': post_data.get('id'),
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'score': post_data.get('score'),
            'url': post_data.get('url'),
            'created_utc': post_data.get('created_utc'),
            'num_comments': post_data.get('num_comments'),
            'selftext': post_data.get('selftext')
        })

    df = pd.DataFrame(posts)
    df.to_csv(f'reddit_posts_{SUBREDDIT}.csv', index=False)
    print(f'Zapisano {len(df)} postów do pliku reddit_posts_{SUBREDDIT}.csv')
else:
    print(f'Błąd podczas pobierania danych: {response.status_code}')