import requests
from bs4 import BeautifulSoup
import datetime
import time
import json

def getArticleFromPage(month, year):
    API_url = "https://www.cracked.com/funny-articles.html?date_year={}&date_month={}".format(str(year), str(month))
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    response = requests.get(API_url, headers = headers)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    soupArticle = soupSite.find_all("h2", class_="title")
    print(response)
    return soupArticle

def getHeadlineDataFormArticle(soupArticle):
    result = []
    for x in soupArticle:
        tmp = x.find("a")
        headline = tmp.get_text()
        article_link = tmp['href']
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
        
def getDataFromPage(month, year):
    print("=>>>>> {}/{}:".format(month, year)) 
    soupArticle = getArticleFromPage(month, year)
    headlineData = getHeadlineDataFormArticle(soupArticle)
    writeFile(headlineData)
    print("Number of data: ",len(headlineData))
    print("\n")

if __name__ == "__main__":
    year = 2021
    year_stop = 2000
    while year > year_stop - 1:
        if year == 2021:
            month = 6
        else:
            month = 12
        while month:
            getDataFromPage(month, year)
            month -= 1
        year -= 1

