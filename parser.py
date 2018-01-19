import requests
import numpy as np
import pandas as pd
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

UserAgent().chrome

def getPageLinks(page_number):
    """
        Returns list of links from current page
        page_number: int/string
    """
    # make link to the search page
    page_link = 'http://knowyourmeme.com/memes/all/page/{}'.format(page_number)

    # request data on it
    response = requests.get(page_link, headers={'User-Agent': UserAgent().chrome})

    if not response.ok:
        # If the server denied, return a blank sheet
        return []

    # получаем содержимое страницы и переводим в суп
    html = response.content
    soup = BeautifulSoup(html,'html.parser')

    # наконец, ищем ссылки на мемы и очищаем их от ненужных тэгов
    meme_links = soup.findAll(lambda tag: tag.name == 'a' and tag.get('class') == ['photo'])
    meme_links = ['http://knowyourmeme.com' + link.attrs['href'] for link in meme_links]

    return meme_links

meme_page = 'http://knowyourmeme.com/memes/doge'
response = requests.get(meme_page, headers={'User-Agent': UserAgent().chrome})
html = response.content
soup = BeautifulSoup(html,'html.parser')

views = soup.find('dd', attrs={'class':'views'})
views = views.find('a').text
views = int(views.replace(',', ''))
print(views)

def getStats(soup, stats):
    """
        Returns the number of views / comments cleared /...
        stats: string
            views/videos/photos/comments

    """

    obj = soup.find('dd', attrs={'class':stats})
    obj = obj.find('a').text
    obj = int(obj.replace(',', ''))

    return obj

views = getStats(soup, stats='views')
videos = getStats(soup, stats='videos')
photos = getStats(soup, stats='photos')
comments = getStats(soup, stats='comments')

print("Просмотры: {}\nВидео: {}\nФото: {}\nКомментарии: {}".format(views, videos, photos, comments))