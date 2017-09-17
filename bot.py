import tweepy, time, sys, datetime
from Functions import beginbot
from Functions import btcitems
from Functions import statisticitems
api = beginbot.start()
if not api:
    print("I had an oopsie :/")
    sys.exit(1)
#Bot is online and connected to twitter account...
print("My name is", api.me().name, "and I'm awake!")
ORIGINALPRICE = btcitems.retrieveprice() #Original Price of BTC
NOW = datetime.datetime.utcnow()
NEXT_TIME = NOW + datetime.timedelta(minutes=1)
statisticitems.STARTVAR = ORIGINALPRICE[0]
while 1:
    #Continuously check for btc price
    time.sleep(12) #Wait 120 Seconds (2mins) 12 for testing
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