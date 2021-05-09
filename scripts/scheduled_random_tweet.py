import json
import random
import time

import schedule
from twitter_bot.twitter_client import TwitterClient


def load_tweet_contents():
    with open('data/tweet_contents.json') as f:
        return json.load(f)


def load_scheduled_times():
    with open('data/schedule.txt') as f:
        return f.readlines()


def tweet(status, media):
    client = TwitterClient()
    return client.post_update(status, media)


def random_tweet():
    tweet_contents = load_tweet_contents()
    selected_tweet = random.choice(tweet_contents)
    status = selected_tweet['status']
    media = selected_tweet['media']
    tweet(status, media)


def main():
    scheduled_times = load_scheduled_times()
    for scheduled_time in scheduled_times:
        schedule.every().day.at(scheduled_time).do(random_tweet)
    while True:
        schedule.run_pending()
        # Wait for one minute
        time.sleep(60)


if __name__ == '__main__':
    main()
