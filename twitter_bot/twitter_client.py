import os

from dotenv import load_dotenv
import twitter


load_dotenv()


class TwitterClient():
    def __init__(self):
        self.consumer_key = os.environ.get('CONSUMER_KEY')
        self.consumer_secret = os.environ.get('CONSUMER_SECRET')
        self.access_token = os.environ.get('ACCESS_TOKEN')
        self.access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
        self.api = self._create_api()

    def _create_api(self):
        return twitter.Api(
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token_key=self.access_token,
            access_token_secret=self.access_token_secret,
        )

    def post_update(self, status='', media=None):
        return self.api.PostUpdate(status=status, media=media)
