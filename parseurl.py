from urllib.parse import urlparse
def parseUrl(url):
    urlSwitch = {
        "twitch.tv":"twitch",
        "youtube.com":"youtube"
    }
    parsedUrl = urlparse(url)    
    result = '{uri.netloc}/'.format(uri=parsedUrl)
    return urlSwitch.get(result)
