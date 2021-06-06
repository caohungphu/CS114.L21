import requests
from bs4 import BeautifulSoup
import datetime
import time
import json

def getArticleFromPage(page):
    API_url = "https://babylonbee.com/news?page={}".format(str(page))
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    response = requests.get(API_url, headers = headers)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    soupArticle = soupSite.find_all("article-card")
    print(response)
    return soupArticle

def getHeadlineDataFormArticle(soupArticle):
    result = []
    for x in soupArticle:
        x = str(x).replace("&quot;", "").replace("</article-card", "").replace("\n", "")
        pos_1 = x.find(":path") + 7
        pos_2 = x.find('" ', pos_1, len(x))
        pos_3 = x.find(":title") + 8
        pos_4 = x.find("'>", pos_3, len(x))
        headline = x[pos_3:pos_4].replace('"','').replace(">", "")
        article_link = "https://babylonbee.com" + x[pos_1:pos_2].replace("'","")
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
    while page < 353: #03/06/2021
        getDataFromPage(page)
        page += 1

