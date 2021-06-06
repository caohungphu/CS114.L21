import requests
from bs4 import BeautifulSoup


def getArticleFromPage(pagenumber):
    urlPage = 'https://www.newyorker.com/humor/borowitz-report/page/' + str(pagenumber)
    response = requests.get(urlPage)
    soupSite = BeautifulSoup(response.text, 'html.parser')
    soupArticle = soupSite.find_all("div", class_="River__riverItemContent___2hXMG")
    return soupArticle

def getHeadlineDataFormArticle(soupArticle):
    result = []
    for x in soupArticle:
        headline = x.find("h4" ,class_= "River__hed___re6RP").get_text()
        article_link = x.find("a")['href']
        is_sarcastic = '1'
        result.append([headline, article_link, is_sarcastic])
    return result

def writeFile(headlineData):
    fileOutput = open("NewYorker.txt", "a", encoding="utf-8")
    for i in headlineData:
        strOut = i[0] + "|https://www.newyorker.com" + i[1] + "|" + i[2] + "\n"
        fileOutput.writelines(strOut)
    fileOutput.close()
        
def getDataFromPage(pagenumber):
    soupArticle = getArticleFromPage(pagenumber)
    headlineData = getHeadlineDataFormArticle(soupArticle)
    writeFile(headlineData)
    print("Number of data: ",len(headlineData))
    print("\n")
    
def main():
    pagenumber = 143 
    while pagenumber:
        getDataFromPage(pagenumber)
        pagenumber -= 1
main()
