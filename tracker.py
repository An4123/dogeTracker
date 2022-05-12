# while price is not hit.
    # every 15 minutes track doge
    # if the price is x near your set price
        # send a text
    # else keep running
# end if price is hit.

import requests
import json
import SMS
import time


def timer(timeValue):
    print("Waiting")
    for i in range(0,timeValue):
        time.sleep(1)

reminderPrice = "600.00"
shares = "4352"

targetHit = False
while targetHit == False:
    req = requests.get("https://sochain.com/api/v2/get_price/DOGE/USD")
    price = req.json()['data']['prices'][0]['price']
    own = float(shares) * float(price)
    priceDiff = own - float(reminderPrice) 
    SMS.send("You own " + str(own) + " of Doge and is " + str(priceDiff) + " away from your set price of $" + reminderPrice)
    if own <= float(reminderPrice): 
        # send reminder that you are below your set price.
        SMS.send("Doge at/below your set price of $ " + reminderPrice)
        targetHit = True
    timer(900) # wait 15 minutes

SMS.send("PROGRAM IS DONE RUNNING")



