#sources: https://stackoverflow.com/questions/60457526/i-am-trying-to-get-my-python-twitter-bot-to-tweet-every-30-minutes-on-the-hour

from my_api_keys import *
from crusoe_dict_script import *
import tweepy
import random as rd

def tweet_check():
    auth = tweepy.OAuthHandler(my_api_key, my_api_secret)
    auth.set_access_token(my_access_token, my_access_token_sec)

    api = tweepy.API(auth)
    retry_counter = 0
    while True:
        if retry_counter < 4:  # If it fails, just try it multiple times in order to be sure lol.
            try:
                api.verify_credentials()
                print("auth ok")
                allGood = True  # this code is shit lol
            except:
                print("Auth error")
                allGood = False

            if allGood == True:
                pair = rd.choice(list(make_crusoe_dict().items()))

                my_tweet = pair
                api.update_status(my_tweet)
                break
            elif allGood == False:
                retry_counter = retry_counter + 1
                continue
        else:
            print("Yeah, the code is f-ed. Sorry, but you need to rewrite it.")
            break

tweet_check()




