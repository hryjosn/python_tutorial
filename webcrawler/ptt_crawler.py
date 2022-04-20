from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
resp = requests.get(url)


def prefix_url(url):
    return 'https://www.ptt.cc' + url


def getTitle(url):
    try:
        html = requests.get(url)
        bs_obj = BeautifulSoup(html.text, features="html.parser")
        boards = bs_obj.findAll('a', {'class': 'board'})

        for ele in boards:
            print("Board Name: ", ele.find("div", {'class': 'board-name'}).text)
            board_link = prefix_url(ele.get('href'))
            print('link: ', board_link)
            my_headers = {'cookie': 'over18=1;'}
            html = requests.get(board_link, headers=my_headers)
            bs_obj = BeautifulSoup(html.text, features="html.parser")
            topic = bs_obj.find('div', {'class': 'title'})
            print('topic:', topic.text.strip())  # strip remove white space
            if topic:
                article_url = topic.find("a").get('href')
                print('article_url:', prefix_url(article_url))
                article_html = BeautifulSoup(requests.get(prefix_url(article_url), my_headers).text, features="html.parser")
                comment = article_html.find('div', {'class': 'push'})
                if comment:
                    print('Author: ', comment.find('span', {'class': 'push-userid'}).text)
                    print('Comment content: ', comment.find('span', {'class': 'push-content'}).text)

    except HTTPError as e:
        return None


getTitle("https://www.ptt.cc/bbs/index.html")
