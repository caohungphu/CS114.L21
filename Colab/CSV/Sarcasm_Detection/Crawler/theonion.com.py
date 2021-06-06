import requests
from bs4 import BeautifulSoup
import datetime
import time

def getTimeTheOnion():
    return int(time.time() * 1000)

def getNewTimeTheOnion(timeStamp):
    return (timeStamp - int(1e9))

def convertTime(timeStamp):
    formatTime = '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.fromtimestamp(timeStamp / 1000).strftime(formatTime)

def getArticleFromPage(timeStamp):
    urlPage = 'https://www.theonion.com/latest?startTime=' + str(timeStamp)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    response = requests.get(urlPage, headers = headers)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    soupArticle = soupSite.find_all("div", class_="cw4lnv-5 aoiLP")
    print(response)
    return soupArticle

def getHeadlineDataFormArticle(soupArticle):
    result = []
    for x in soupArticle:
        headline = x.find("h2").get_text()
        article_link = x.find("a")['href']
        is_sarcastic = '1'
        result.append([headline, article_link, is_sarcastic])
    return result

def writeFile(headlineData):
    fileOutput = __file__.replace(".py", ".txt")
    f = open(fileOutput, "a", encoding="utf-8")
    for i in headlineData:
        strOut = i[0] + "|" + i[1] + "|" + i[2] + "\n"
        f.writelines(strOut)
    f.close()
        
def getDataFromPage(timeStamp):
    print("=>>>>> ",convertTime(timeStamp))
    soupArticle = getArticleFromPage(timeStamp)
    headlineData = getHeadlineDataFormArticle(soupArticle)
    writeFile(headlineData)
    print("Number of data: ",len(headlineData))
    print("\n")

if __name__ == "__main__":
    k = 1000
    timeNow = getTimeTheOnion()
    while k:
        getDataFromPage(timeNow)
        timeNow = getNewTimeTheOnion(timeNow)
        k -= 1

