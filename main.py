# coding:utf-8
import requests
from bs4 import BeautifulSoup
from lxml import etree
import re

host = 'http://dictionary.cambridge.org/dictionary/english-chinese-simplified/'
word = 'word'
url = host+word

r = requests.get(url)
# soup = BeautifulSoup(r.text)
# word_name_css = '#entryContent > div.cdo-dblclick-area > div > div.di-body > div > div > div > div.pos-header > h2 > span.headword > span'
# word_name = soup.select(word_name_css)
html = etree.HTML(r.text)
word_name_xpath = '//*[@id="entryContent"]/div[3]/div/div[2]/div/div/div[1]/div[1]/h2/span[1]/span'
word_name = html.xpath(word_name_xpath)[0].text
word_meaning_xpath = '//*[@id="entryContent"]/meta[1]/@content'
word_meaning = html.xpath(word_meaning_xpath)[0]
splited_meaning = re.split(u'[\:\.\uff1b]',word_meaning.replace(' ',''))
meaning_count = 0
new_content = '###%s\n'%word_name 
for meaning in splited_meaning[1:-2]:
    meaning_count += 1
    new_content += '\t\t%d.\t%s\n'%(meaning_count, meaning)
print new_content
