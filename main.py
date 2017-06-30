# coding:utf-8
import requests
from lxml import etree
import re
import copy
import clipboard
from time import sleep
from datetime import datetime

def get_word_meaning(word):
    url = 'http://dictionary.cambridge.org/dictionary/english-chinese-simplified/%s'%word
    r = requests.get(url)
    html = etree.HTML(r.text)
    word = {}
    word_xpath = {}
    word_xpath['name'] = '//*[@id="entryContent"]/div[3]/div/div[2]/div/div/div[1]/div[1]/h2/span[1]/span'
    word['name'] = html.xpath(word_xpath['name'])[0].text
    word_xpath['honetis_symbol'] = '//*[@id="entryContent"]/div[3]/div/div[2]/div/div/div/div[1]/span[2]/span[2]/span/span'
    word['honetis_symbol'] = html.xpath(word_xpath['honetis_symbol'])[0].text
    word_xpath['meaning'] = '//*[@id="entryContent"]/meta[1]/@content'
    word['meaning'] = re.split(u'[\:\.\uff1b]',html.xpath(word_xpath['meaning'])[0].replace(' ',''))
    meaning_count = 0
    new_content = '###%s\t|%s|\n'%(word['name'],word['honetis_symbol'])
    for meaning in word['meaning'][1:-2]:
        meaning_count += 1
        new_content += '\t%d.\t%s\n'%(meaning_count, meaning)
    print new_content
    return new_content


def is_a_word(word):
    word_test = re.compile('^[a-z]+$')
    if word_test.match(word):
        print 'it is a word'
        return True
    else:
        print "Not a word"
        return False

file_name = 'new_word@%s.md'%datetime.today().strftime('%m-%d')
with open(file_name,'a') as word_file:
    word_record = ''
    while True:
        
        word = clipboard.paste().replace('\t','').replace(' ','').lower()
        word_test = re.compile('[a-zA-Z]+')
        if word != word_record:
            if is_a_word(word):
                new_content = get_word_meaning(word)
                word_file.write(new_content.encode('utf-8'))
            word_record = copy.copy(word)
        sleep(1)



