__author__ = 'Ofir'

import requests
import re
FRST = "http://www.theuselessweb.com/"
urls = []
newReg = "http[s]?:\/\/[www\.]?[a-zA-Z0-9@:%_\+~#=\.]{2,256}\.[a-zA-Z0-9\.]{2,10}\/"
lastPos = 0
visited = []
def extractURLs(code):
    global newReg
    log = open("log.txt",'a')
    extract = re.findall(newReg,code)
    extract = list(set(extract))
    if len(extract) != 0:
        for i in range(0,len(extract)):
            if requests.get(extract[i]).status_code == 200:
                if extract[i] not in urls:
                    urls.append(extract[i])
                log.write(extract[i])
                log.write("\n")
    log.close()

def initiate(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            visited.append(url)
            extractURLs(r.text)
            hop()
        else:
            print("Not ok",r.status_code,"at",url)
            hop()
    except:
        print("ERROR AT",url)
        hop()
def hop():
    global lastPos
    global urls
    for i in range(lastPos,len(urls)):
        lastPos += 1
        if(urls[i] not in visited):
            print("INITATING ",urls[i])
            initiate(urls[i+1])
def main():
    firstURL = FRST
    initiate(firstURL)
if __name__ == "__main__":
    main()