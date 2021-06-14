import requests
from bs4 import BeautifulSoup

def getArticleFromPage(x):
    urlPage = 'https://time.com/html-sitemap/time-section-world/part/' + str(x)
    response = requests.get(urlPage)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    soupArticle = soupSite.find("div", class_="ti-sitemap-list clearfix").findAll("li")
    return soupArticle

def getHeadlineDataFormArticle(soupArticle):
    result = []
    for x in soupArticle:
        tmp = x.find("a")
        headline = tmp.get_text()
        article_link = tmp['href'][:-1]
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
        
def getDataFromPage(page):
    print("=>>>>> Page: {}".format(page)) 
    soupArticle = getArticleFromPage(page)
    headlineData = getHeadlineDataFormArticle(soupArticle)
    writeFile(headlineData)
    print("Number of data: ",len(headlineData))
    print("\n")

if __name__ == "__main__":
    page = 1
    while page < 210: #14/06/2021
        getDataFromPage(page)
        page += 1
