import requests
from bs4 import BeautifulSoup
import datetime
import time
import json

def getArticleFromPage(month, year):
    API_KEY = 'VgAeXa43ETi5AMY6B8fbSWiIdw4cxEop'
    API_url = "https://api.nytimes.com/svc/archive/v1/{}/{}.json?api-key={}".format(str(year), str(month), API_KEY)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    response = requests.get(API_url, headers = headers)
    return response.json()['response']['docs']

def getHeadlineDataFormArticle(soupArticle):
    result = []
    for x in soupArticle:
        headline = x['headline']['main']
        article_link = x['web_url']
        is_sarcastic = '0'
        result.append([headline, article_link, is_sarcastic])
    return result

def writeFile(headlineData):
    fileOutput = __file__.replace(".py", ".txt")
    f = open(fileOutput, "a", encoding="utf-8")
    for i in headlineData:
        strOut = i[0] + "|" + i[1] + "|" + i[2] + "\n"
        f.writelines(strOut)
    f.close()
        
def getDataFromPage(month, year):
    print("=>>>>> {}/{}:".format(month, year)) 
    soupArticle = getArticleFromPage(month, year)
    headlineData = getHeadlineDataFormArticle(soupArticle)
    writeFile(headlineData)
    print("Number of data: ",len(headlineData))
    print("\n")

if __name__ == "__main__":
    year = 2021
    year_stop = 2020
    while year > year_stop - 1:
        if year == 2021:
            month = 6
        else:
            month = 12
        while month:
            getDataFromPage(month, year)
            month -= 1
        year -= 1

