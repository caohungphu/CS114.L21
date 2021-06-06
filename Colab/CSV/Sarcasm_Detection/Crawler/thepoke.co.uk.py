import requests
from bs4 import BeautifulSoup
import datetime
import time

def getArticleFromPage(x):
    urlPage = 'https://www.thepoke.co.uk/category/news/page/' + str(x)
    response = requests.get(urlPage)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    soupArticle = soupSite.find_all("article", class_="boxgrid")
    return soupArticle

def getHeadlineDataFormArticle(soupArticle):
    result = []
    for x in soupArticle:
        if x.find("p"):
            headline = x.find("p").get_text()
            article_link = x.find("a")['href']
            article_link = article_link[:-1]
            is_sarcastic = '1'
            result.append([headline, article_link, is_sarcastic])
    return result

def writeFile(headlineData):
    fileOutput = open("TheOnion.txt", "a", encoding="utf-8")
    for i in headlineData:
        strOut = i[0] + "|" + i[1] + "|" + i[2] + "\n"
        fileOutput.writelines(strOut)
    fileOutput.close()
        
def getDataFromPage(timeStamp):
    print("=>>>>> ")
    soupArticle = getArticleFromPage(timeStamp)
    headlineData = getHeadlineDataFormArticle(soupArticle)
    writeFile(headlineData)
    print("Number of data: ",len(headlineData))
    print("\n")
    
def main():
    k = 500 #Thay cho nay de lay duoc nhieu hon
    x = 1
    while k:
        getDataFromPage(x)
        x +=1
        k -= 1

main()
