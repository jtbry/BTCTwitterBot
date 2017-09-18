import requests
import os
import urllib.request
import json
import imghdr
import codecs
from bs4 import BeautifulSoup
from Functions import statisticitems

def retrieveprice():
    """Retrieve current bitcoin price using coindesk.com"""
    url = "https://api.coindesk.com/v1/bpi/currentprice.json" #URL to coindesk API
    urlrequest = urllib.request.urlopen(url)
    pagereader = codecs.getreader("utf-8")
    pagedata = json.load(pagereader(urlrequest))
    urlrequest.close()

    #Data from json script retrieved process it
    usdrate = pagedata['bpi']['USD']['rate'] #Price in USD
    eurrate = pagedata['bpi']['EUR']['rate'] #Price in EUR
    gbprate = pagedata['bpi']['GBP']['rate'] #Price in GBP
    updatet = pagedata['time']['updated'] #Date time it was updated!
    info = [usdrate, eurrate, gbprate, updatet]
    return info

def is_validprice(newdata, olddata):
    """Check if price has changed +/- 5"""
    math = float(olddata[0].replace(',', '')) - float(newdata[0].replace(',', ''))
    if math >= 5:
        #Price dropped
        print("Price dropped from", olddata[0], "to", newdata[0], "with a difference of", math)
        statisticitems.CURRENTVAR = str(round(float(newdata[0].replace(',', '')), 2))
        statisticitems.PERCENTVAR = str(round(float(getmath(newdata, olddata)[3]), 2))
        statisticitems.updatedata()
        return "down"
    elif math <= -5:
        #Price raised
        print("Price rose from", olddata[0], "to", newdata[0], "with a difference of", math)
        statisticitems.CURRENTVAR = str(round(float(newdata[0].replace(',', '')), 2))
        statisticitems.PERCENTVAR = str(round(float(getmath(newdata, olddata)[3]), 2))
        statisticitems.updatedata()
        return "up"   
    elif math != 0:
        statisticitems.CURRENTVAR = str(round(float(newdata[0].replace(',', '')), 2))
        statisticitems.PERCENTVAR = str(round(float(getmath(newdata, olddata)[3]), 2))
        statisticitems.updatedata()
    else:
        #Price didn't change by +/- 5
        print("Price didn't change...", "(", olddata[0], "|", newdata[0], ")")
        return "neither"

def getmath(ndata, odata):
    """Retrieve the drop percentage and how much it's dropped by"""
    difference = float(odata[0].replace(',', '')) - float(ndata[0].replace(',', ''))
    percentchng = (difference / float(odata[0].replace(',', ''))) * 100
    info = [ndata, odata, difference, percentchng]
    return info

def preparestring(math, oldprice, newprice, var, alldata):
    elements = ["rose", "dropped"]
    for data in alldata:
        for index, element in enumerate(data[:-1]):
            data[index] = str(round(float(data[index].replace(',', '')), 2))
    string = "Bitcoin " + elements[var] + " by %" + str(round(math[3], 3)).replace('-', '') +"\n" + "USD: " + alldata[0][0] + " -> " + alldata[1][0] + "\nEUR: " + alldata[0][1] + " -> " + alldata[1][1] + "\nGBP: " + alldata[0][2] + " -> " + alldata[1][2] + "\nUpdated on " + alldata[1][3] 
    return string


# Bitcoin has {droped/rose}
# USD: oldprice -> newprice
# EUR: oldprice -> newprice
# GBP: oldprice -> newprice
# {dropped/rose} by {percent}
# Updated {date}
#
#
#
