import requests
from bs4 import BeautifulSoup
import datetime
import time
import json

def getArticleFromPage(day, month, year):
    API_url = "https://rochdaleherald.co.uk/{}/{}/{}".format(str(year), str(month),str(day))
    print(API_url)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    response = requests.get(API_url, headers = headers)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    soupArticle = soupSite.find_all("h3", class_="entry-title td-module-title")
    print(response)
    return soupArticle

def getHeadlineDataFormArticle(soupArticle):
    result = []
    for x in soupArticle:
        tmp = x.find("a")
        headline = tmp['title']
        article_link = tmp['href']
        article_link = article_link[:-1]
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
        
def getDataFromPage(day, month, year):
    print("=>>>>> {}/{}/{}:".format(day,month, year)) 
    soupArticle = getArticleFromPage(day,month, year)
    headlineData = getHeadlineDataFormArticle(soupArticle)
    writeFile(headlineData)
    print("Number of data: ",len(headlineData))
    print("\n")

if __name__ == "__main__":
    year = 2021
    year_stop = 2015
    while year > year_stop - 1:
        if year == 2021:
            month = 6
        else:
            month = 12
        while month:
            if month in [1,2,3,4,5,6,7,8,9]:
                monthh = '0' + str(month)
            else:
                monthh = month
            day = 31
            while day:
                if day in [1,2,3,4,5,6,7,8,9]:
                    dayy =  '0' + str(day)
                else:
                    dayy = day
                getDataFromPage(dayy, monthh, year)
                day -= 1
            month -= 1
        year -= 1