import argparse

from twitter_bot.twitter_client import TwitterClient


def tweet(status, media):
    client = TwitterClient()
    return client.post_update(status, media)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t', '--status', type=str, required=True, help='The status to tweet')
    parser.add_argument(
        '-m', '--media', type=str, help='The media URL to tweet')
    args = parser.parse_args()
    tweet(args.status, args.media)


if __name__ == '__main__':
    main()
