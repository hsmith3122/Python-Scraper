import scraper
import message
from datetime import datetime
import time as time
import random


def getNewInStock(cursites, lastsites):
    newinstock = []
    for i in range(len(cursites)):
        if cursites[i] and not lastsites[i]:
            newinstock.append(cursites[i])

    return newinstock

def getNewOutStock(cursites, lastsites):
    newoutstock = []
    for i in range(len(cursites)):
        if lastsites[i] and not cursites[i]:
            newoutstock.append(lastsites[i])

    return newoutstock


firstHour = 9
lastHour = 16
interval = 15  # seconds

lastsites = [''] * scraper.numConsoles

while True:
    now = datetime.now()
    hour = int(now.strftime('%H'))
    minutes = int(now.strftime('%M'))
    seconds = int(now.strftime('%S'))
    milli = int(now.strftime('%f'))

    if hour < firstHour or hour > lastHour:
        sleep = {
            'seconds': 60 - seconds,
            'minutes': 59 - minutes,
            'hours'  : 23 - hour,
        }
        print("Sleeping for:\n\t" + str(sleep['seconds']) + ' seconds\n\t' + str(sleep['minutes']) + ' minutes\n\t' + str(sleep['hours']) + ' hours')
        time.sleep(
            sleep['seconds'] +
            (sleep['minutes'] * 60) +
            (sleep['hours'] * 3600)
        )

    # iterate until lastHour has passed
    print("Starting Scrape: " + datetime.now().strftime('%X'))
    while int(datetime.now().strftime("%H")) <= lastHour:
        cursites = scraper.scrapeAll()
        justin = getNewInStock(cursites, lastsites)
        justout = getNewOutStock(cursites, lastsites)

        text = ''

        if len(justin):
            text += '\n\nJust In:'
            for item in justin:
                text += item

        if len(justout):
            if text:
                text += '\n\n'
            text += '\n\n'

            text += 'Just Out:'
            for item in justout:
                text += item
            if text:
                print("Text Sent:\n\n" + text)
                message.sendText(message.phone_herb, text)

        time.sleep(random.randint(0, interval * 2) + 5)
        lastsites = cursites

