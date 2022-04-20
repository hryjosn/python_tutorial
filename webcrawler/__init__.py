from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError


def getTitle(url):
    try:
        html = urlopen(url)
        bs_obj = BeautifulSoup(html, features="html.parser")
        for a in bs_obj.find_all('a', href=True):
            print(a.get('href'))
            # if(a.get('href').startWith('https')){
            #     html = urlopen(a.get('href'))
            #     bs_obj = BeautifulSoup(html, features="html.parser")
            #     print("new page bsobj:",bs_obj)
            # }else{
            #     html = urlopen("https://en.wikipedia.org" + a.get('href'))
            #     bs_obj = BeautifulSoup(html, features="html.parser")
            #     print("new page bsobj:", bs_obj)
            # }
    except HTTPError as e:
        return None


getTitle("https://en.wikipedia.org/wiki/Wiki")
