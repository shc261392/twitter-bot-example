# twitter-bot-example
A minimum example for how to run a Python Twitter bot to tweet automatically.

# Quickstart

1. Get a Twitter account
2. Go to [Twitter Dev Dashboard](https://developer.twitter.com/en/portal/projects-and-apps)
    1. Create an App and enter the App name (bot name)
    2. Save the `API Key` and `API Secret Key` to somewhere safe
    3. Click `App Settings`
    4. Click `Keys and Tokens` tab
    5. Click the `Generate` button in `Access Token and Secret` section
    6. Save the `Access token` and `Access token secret` to somewhere safe
3. Clone the twitter-bot-example

```
$ git clone git@github.com:shc261392/twitter-bot-example.git
$ cd twitter-bot-example
```

4. Create your `.env` file by

```
$ cp .env.example .env
```

5. Fill the `.env` file with your saved keys. For example, if your `API key` is `111111`, your `API secret key` is `222222`, your `Access token` is `333333`, your `Access token secret` is `444444`, it should look like this:

```
CONSUMER_KEY=111111
CONSUMER_SECRET=222222
ACCESS_TOKEN=333333
ACCESS_TOKEN_SECRET=444444
```

6. Create and activate a virtual environment

```
$ python3 -m venv venv
$ source venv/bin/activate
```

7. Install dependencies and install the package in editable mode

```
(venv)$ python3 -m pip install -e .
```

8. You can now try to tweet with the bot

Tweet (text only)

```
(venv)$ simple_tweet -t 'This is the content of tweet'
```

Tweet (text and image)

```
(venv)$ simple_tweet -t 'This is a tweet with image' -m https://d1e00ek4ebabms.cloudfront.net/production/846fa298-c016-465f-b73e-0591df79ec98.png
```

Random tweet chosen from `data/tweet_contents.json`

```
(venv)$ random_tweet
```

Random tweet chosen from `data/tweet_contents.json`, scheduled to tweet on all times listed in `data/schedule.txt`

```
(venv)$ scheduled_random_tweet
```


