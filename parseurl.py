from urllib.parse import urlparse
from parseYouTube import parseYouTube
def parseUrl(url):
    urlSwitch = {
        "www.twitch.tv":"parseTwitch",
        "www.youtube.com":"parseYouTube"
    }
    parsedUrl = urlparse(url)    
    result = '{uri.netloc}'.format(uri=parsedUrl)
    print(result)
    parseFunction = urlSwitch.get(result, lambda: "unsupport website")
    #print("\n" + str(parseFunction) + "\n")
    return str(parseFunction)
