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

meme_links = getPageLinks(1)
print (meme_links[:2])