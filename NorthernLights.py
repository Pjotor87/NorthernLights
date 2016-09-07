#!/usr/bin/env python
import datetime
try:
    # For Python 3.0 and later
    import urllib.request as urllib2
except ImportError:
    # Fall back to Python 2's urllib2
    import urllib2
from bs4 import BeautifulSoup
import os
import sys
import RoboMail
import ApplicationSettings

def broadcast(kpValue):
    # Open file and add each line with trimmed leading and trailing whitespace as a subscriber in list.
    subscribers = []
    with open(os.path.dirname(os.path.realpath(sys.argv[0]))+"/Subscribers.txt") as subscribersFile:
        subscribers = [line.strip() for line in subscribersFile]
    # Declare an empty string that gathers exception messages in the coming loop.
    mailRecipientExeptionMessages = ''
    # Loop through subscribers and send email to each one.
    for subscriberMailAdress in subscribers:
        if (subscriberMailAdress):
            try:
                RoboMail.send_gmail_message_from_robot(
                    subscriberMailAdress, 
                    "Aurora Borealis update",
                    (
                        "Greetings from Peter Anderssons aurora borealis robot!<br /><br />"
                        "The condtions are right for seeing the aurora borealis in Stockholm this hour.<br /><br />"
                        "Current KP value: <b>"+str(kpValue)+"</b><br /><br />"
                        "Find out more by visiting: <a href='http://www.aurora-service.eu/aurora-forecast'>This link</a>"
                    ), 
                    False, 
                    None)
            except Exception as sendMailException:
                mailRecipientExeptionMessages += (
                    "Something went wrong when sending mail to recipient: " + 
                    subscriberMailAdress + 
                    "<br /><br />exception: " + 
                    str(sendMailException) + "<br />"
                )
    # Send the gathered exceptions if there are any.
    if mailRecipientExeptionMessages:
        RoboMail.send_gmail_message_from_robot(
            ApplicationSettings.settings.Get("AdminEmail"),
            "Aurora Borealis update mail recipient exception",
            mailRecipientExeptionMessages,
            False,
            None)

def main():
    try:
        auroraBorealisForecastMarkup = BeautifulSoup((str(urllib2.urlopen(urllib2.Request("http://www.aurora-service.eu/aurora-forecast", headers={'User-Agent':"Magic Browser"})).read())), 'html.parser')
        kpValue = float(str(auroraBorealisForecastMarkup.select('div.transtab div#hourly p h4 span')[0]).split('>')[1].split('<')[0].replace("Kp", "").strip())
        if kpValue >= 6:
            broadcast(kpValue)
    except Exception as ex:
        RoboMail.send_gmail_message_from_robot(
            ApplicationSettings.settings.Get("AdminEmail"),
            "Aurora Borealis update general exception",
            (
                "Exception:<br /><br />"+
                str(ex)
            ),
            False,
            None)
    
main()