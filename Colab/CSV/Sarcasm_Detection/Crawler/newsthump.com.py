import requests
from bs4 import BeautifulSoup
import datetime
import time
import json

def getArticleFromPage(day, month, year):
    API_url = "https://newsthump.com/{}/{}/{}/".format(str(year), str(month), str(day))
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    response = requests.get(API_url, headers = headers)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    soupArticle = soupSite.find_all("h2", class_="entry-title")
    print(response)
    return soupArticle

def getHeadlineDataFormArticle(soupArticle):
    result = []
    for x in soupArticle:
        tmp = x.find("a")
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
        
def getDataFromPage(day,month, year):
    print("=>>>>> {}/{}/{}:".format(day, month, year)) 
    soupArticle = getArticleFromPage(day, month, year)
    headlineData = getHeadlineDataFormArticle(soupArticle)
    writeFile(headlineData)
    print("Number of data: ",len(headlineData))
    print("\n")
    
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)    
  
def getDate(month, year):
    day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        day_of_month[2] = 29
    return day_of_month[month]
    
if __name__ == "__main__":
    year = 2021
    year_stop = 1999
    while year > year_stop - 1:
        month = 12
        if year == 2021:
            month = 6
        while month:
            day = getDate(month, year)
            if year == 2021 and month == 6:
                day = 3
            while day: 
                getDataFromPage(day, month, year)
                day -= 1
            month -= 1
        year -= 1

