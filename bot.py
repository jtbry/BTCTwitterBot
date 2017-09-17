import tweepy, time, sys, datetime

# We are storing twitter credentials in it's own file
from credentials import CONSUM_KEY, CONSUM_SEC, ACCESS_KEY, ACCESS_SEC

from Functions import btcitems
from Functions import statisticitems
from Functions import fake_data_generator
from Functions import fake_api

# Use the fake generator instead of pulling data from the 
# coindesk api
SETTING_USE_FAKE_GENERATOR = True

# Allow running without actually connecting to twitter to post results
SETTING_DONT_CONNECT_TO_TWITTER = True

def authenticate():
    """ Authenticate with twitter, and return handler if succesful. """
    if SETTING_DONT_CONNECT_TO_TWITTER:
        api = fake_api.FakeAPI()

        return api

    authentication = tweepy.OAuthHandler(CONSUM_KEY, CONSUM_SEC)
    authentication.set_access_token(ACCESS_KEY, ACCESS_SEC)
    api = tweepy.API(authentication)
    return api

api = authenticate()
if not api:
    print("I had an oopsie :/")
    sys.exit(1)

#Bot is online and connected to twitter account...
print("My name is", api.me().name, "and I'm awake!")

if SETTING_USE_FAKE_GENERATOR:
    ORIGINALPRICE = fake_data_generator.retrieveprice()
else:
    ORIGINALPRICE = btcitems.retrieveprice() #Original Price of BTC

NOW = datetime.datetime.utcnow()
NEXT_TIME = NOW + datetime.timedelta(minutes=1)
statisticitems.STARTVAR = ORIGINALPRICE[0]

while 1:
    #Continuously check for btc price
    time.sleep(12) #Wait 120 Seconds (2mins) 12 for testing

    if SETTING_USE_FAKE_GENERATOR:
        PRICEDATA = fake_data_generator.retrieveprice()
    else:
        PRICEDATA = btcitems.retrieveprice() #New Price of BTC

    VALID_DATA = btcitems.is_validprice(PRICEDATA, ORIGINALPRICE)
    if VALID_DATA == "up":
        #Price went up
        MATHDATA = btcitems.getmath(PRICEDATA, ORIGINALPRICE)
        ALLDATA = [ORIGINALPRICE, PRICEDATA]
        preparedstring = btcitems.preparestring(MATHDATA, ORIGINALPRICE[0], PRICEDATA[0], 0, ALLDATA)
        api.update_status(status=preparedstring[:140])
        ORIGINALPRICE = PRICEDATA
    elif VALID_DATA == "down":
        #Price went down
        MATHDATA = btcitems.getmath(PRICEDATA, ORIGINALPRICE)
        ALLDATA = [ORIGINALPRICE, PRICEDATA]
        preparedstring = btcitems.preparestring(MATHDATA, ORIGINALPRICE[0], PRICEDATA[0], 1, ALLDATA)
        api.update_status(status=preparedstring[:140])
        ORIGINALPRICE = PRICEDATA
    if(datetime.datetime.utcnow() > NEXT_TIME):
        #statisticitems.writetofile("A minute has passed...")
        NOW = datetime.datetime.utcnow()
        NEXT_HOUR = NOW + datetime.timedelta(minutes=1)    
    #else price didn't change...
