import requests
from bs4 import BeautifulSoup


def getArticleFromPage(pagenumber):
    urlPage = 'https://www.euronews.com/news/asia?p=' + str(pagenumber)
    response = requests.get(urlPage)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    soupArticle = soupSite.find_all("div", class_="m-object__description")
    return soupArticle

def getHeadlineDataFormArticle(soupArticle):
    result = []
    for x in soupArticle:
        headline = x.find("a")['title']
        article_link = x.find("a")['href']
        is_sarcastic = '0'
        result.append([headline, article_link, is_sarcastic])
    return result

def writeFile(headlineData):
    fileOutput = open("euronews.com.txt", "a", encoding="utf-8")
    for i in headlineData:
        strOut = i[0] + "|https://www.euronews.com" + i[1] + "|" + i[2] + "\n"
        fileOutput.writelines(strOut)
    fileOutput.close()
        
def getDataFromPage(pagenumber):
    soupArticle = getArticleFromPage(pagenumber)
    headlineData = getHeadlineDataFormArticle(soupArticle)
    writeFile(headlineData)
    print("Number of data: ",len(headlineData))
    print("\n")
    
def main():
    pagenumber = 415 
    while pagenumber:
        getDataFromPage(pagenumber)
        pagenumber -= 1
main()
