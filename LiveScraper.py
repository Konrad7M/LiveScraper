from parseYouTube import *
from parseUrl import *
from parseTwitch import *

def main():
    url = sys.argv[1]
    downloadFunctionName = parseUrl(url)
    possibles = globals().copy()
    possibles.update(locals())
    downloadFunction = possibles.get(downloadFunctionName)
    downloadFunction(url)

if __name__ == "__main__":
    main()
