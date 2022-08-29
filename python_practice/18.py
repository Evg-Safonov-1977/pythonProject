import requests
import lxml.html
from lxml import etree

html = requests.get('https://worldoftanks.ru/').content

tree = etree.parse('World of Tanks – Бесплатная Онлайн-игра про Танки.html',
                   lxml.html.HTMLParser())

ul = tree.findall(
     'body/div[1]/div/div[4]/div[2]/div[1]/div/div/div[3]/div[2]')

for li in ul:
    a = li.find('a')
    time = li.find('time')
    print(time.get('datetime'), a.text)


# import requests
# import lxml.html
# from lxml import etree
#
# html = requests.get('https://worldoftanks.ru/').content
#
# etree = lxml.html.document_fromstring(html)
# title = etree.xpath(
#       '/html/head/title/text()')
# print(title)

