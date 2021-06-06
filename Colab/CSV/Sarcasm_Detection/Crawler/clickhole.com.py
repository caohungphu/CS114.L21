import requests
from bs4 import BeautifulSoup
import datetime
import time
import json

def getArticleFromPage(page):
    API_url = "https://clickhole.com/page/{}/".format(str(page))
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    response = requests.get(API_url, headers = headers)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    soupArticle = soupSite.find_all("article")
    print(response)
    return soupArticle

def getHeadlineDataFormArticle(soupArticle):
    result = []
    for x in soupArticle:
        tmp = x.find("h2", class_="post-title").find("a")
        headline = tmp.get_text()
        article_link = tmp['href'][:-1]
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
        
def getDataFromPage(page):
    print("=>>>>> Page: {}".format(page)) 
    soupArticle = getArticleFromPage(page)
    headlineData = getHeadlineDataFormArticle(soupArticle)
    writeFile(headlineData)
    print("Number of data: ",len(headlineData))
    print("\n")

if __name__ == "__main__":
    page = 1
    while page < 1171: #03/06/2021
        getDataFromPage(page)
        page += 1

