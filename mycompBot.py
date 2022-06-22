
import time
import config
import tweepy

auth = tweepy.OAuthHandler(config.consumerKey, config.consumerKeySecret)
auth.set_access_token(config.accessToken, config.accessTokenSecret)

api = tweepy.API(auth)

searched_tweets = [status for status in tweepy.Cursor(api.search_tweets, q="leetcode").items(10)]

for s in searched_tweets:
    sn = s.user.screen_name
    print(s.id)
    m = "https://www.youtube.com/watch?v=4YcR622e6P4"
    api.update_status(status=m, in_reply_to_status_id = s.id, auto_populate_reply_metadata=True)
    time.sleep(5)