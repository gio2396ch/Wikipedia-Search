from bs4 import BeautifulSoup
import requests

con = str(input("What are you looking for? "))


def site(con):
    url = requests.get("http://wikipedia.org/wiki/"+con).text
    bsObj = BeautifulSoup(url, "html.parser")


    res = bsObj.findAll('p')
    print(res)

site(con)

