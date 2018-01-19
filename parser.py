import requests
import numpy as np
import pandas as pd
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

UserAgent().chrome

page_link = 'http://knowyourmeme.com/memes/all/page/1'
response = requests.get(page_link, headers={'User-Agent': UserAgent().chrome})
print (response)

html = response.content
soup = BeautifulSoup(html,'html.parser')

obj = soup.find(lambda tag: tag.name == 'a' and tag.get('class') == ['photo']) #removes the passage of unnecessary links

meme_links = soup.findAll(lambda tag: tag.name == 'a' and tag.get('class') == ['photo']) #All objects that contain links to pages with memes

meme_links = [link.attrs['href'] for link in meme_links]
print(meme_links[:10])
