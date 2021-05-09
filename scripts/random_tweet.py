import json
import random

from twitter_bot.twitter_client import TwitterClient


def load_tweet_contents(filepath):
    with open(filepath) as f:
        return json.load(f)


def tweet(status, media):
    client = TwitterClient()
    return client.post_update(status, media)


def random_tweet():
    tweet_contents = load_tweet_contents('data/tweet_contents.json')
    selected_tweet = random.choice(tweet_contents)
    tweet(selected_tweet['status'], selected_tweet['media'])


def main():
    random_tweet()


if __name__ == '__main__':
    main()
