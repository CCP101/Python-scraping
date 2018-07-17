from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


# Retrieves a list of all Internal links found on a page
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


# Retrieves a list of all external links found on a page
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # Finds all links that start with "http" or "www" that do
    # not contain the current URL
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getRandomExternalLink(internalLinks[random.randint(0,
                                                                  len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("https://github.com")
    print("Random external link is: " + externalLink)
    followExternalOnly(externalLink)


followExternalOnly("https://github.com")
'''
Random external link is: http://electron.atom.io/
Random external link is: https://opensource.guide/
Random external link is: https://atom.io
'''

# def followExternalOnly(startingSite):
#     externalLink = getRandomExternalLink("http://oreilly.com")
#     print("Random external link is: " + externalLink)
#     followExternalOnly(externalLink)


# followExternalOnly("http://oreilly.com")


'''
Random external link is: https://www.safaribooksonline.com/public/free-trial/
Random external link is: https://www.safaribooksonline.com/public/free-trial/
Random external link is: https://www.linkedin.com/company/oreilly-media
Random external link is: https://www.youtube.com/user/OreillyMedia
Random external link is: https://www.facebook.com/OReilly/
Random external link is: https://www.linkedin.com/company/oreilly-media
Random external link is: https://play.google.com/store/apps/details?id=com.safariflow.queue
Random external link is: https://www.linkedin.com/company/oreilly-media
Random external link is: https://www.safaribooksonline.com/public/free-trial/
Random external link is: https://www.youtube.com/user/OreillyMedia
Random external link is: https://www.safaribooksonline.com/team-setup/
Random external link is: https://www.safaribooksonline.com/public/free-trial/
Random external link is: https://twitter.com/oreillymedia
Random external link is: https://play.google.com/store/apps/details?id=com.safariflow.queue
Random external link is: https://play.google.com/store/apps/details?id=com.safariflow.queue
Random external link is: https://www.facebook.com/OReilly/
Random external link is: https://www.safaribooksonline.com/team-setup/
Random external link is: https://www.facebook.com/OReilly/
Random external link is: https://itunes.apple.com/us/app/safari-to-go/id881697395
Random external link is: https://www.linkedin.com/company/oreilly-media
Random external link is: https://www.linkedin.com/company/oreilly-media
Random external link is: https://www.safaribooksonline.com/public/free-trial/
Random external link is: https://www.safaribooksonline.com/public/free-trial/
Random external link is: https://itunes.apple.com/us/app/safari-to-go/id881697395
Random external link is: https://itunes.apple.com/us/app/safari-to-go/id881697395
Random external link is: https://www.linkedin.com/company/oreilly-media
Random external link is: https://play.google.com/store/apps/details?id=com.safariflow.queue
Random external link is: https://www.facebook.com/OReilly/
Random external link is: https://www.youtube.com/user/OreillyMedia
Random external link is: https://itunes.apple.com/us/app/safari-to-go/id881697395
Random external link is: https://itunes.apple.com/us/app/safari-to-go/id881697395
Random external link is: https://www.linkedin.com/company/oreilly-media
Random external link is: https://www.facebook.com/OReilly/
Random external link is: https://play.google.com/store/apps/details?id=com.safariflow.queue
Random external link is: https://www.facebook.com/OReilly/
Random external link is: https://www.linkedin.com/company/oreilly-media
Random external link is: https://play.google.com/store/apps/details?id=com.safariflow.queue
Random external link is: https://twitter.com/oreillymedia
Random external link is: https://itunes.apple.com/us/app/safari-to-go/id881697395
'''
