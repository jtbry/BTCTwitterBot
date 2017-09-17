import tweepy, os, sys, time

def start():
        #Bot Info
        CONSUM_KEY = ""                                #Consumer Key
        CONSUM_SEC = ""       #Consumer Secret 
        ACCESS_KEY = ""       #Access Key    
        ACCESS_SEC = ""            #Access Secret
        #Set key details
        authentication = tweepy.OAuthHandler(CONSUM_KEY, CONSUM_SEC)
        authentication.set_access_token(ACCESS_KEY, ACCESS_SEC)
        api = tweepy.API(authentication)
        return api