import requests
from lxml import html

pageContent=requests.get('https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_judo')
tree = html.fromstring(pageContent.content)

goldWinners=tree.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr/td[2]/a[1]/text()')
silverWinners=tree.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr/td[3]/a[1]/text()')
#bronzeWinner we need rows where there's no rowspan - note XPath
bronzeWinners=tree.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr/td[4]/a[1]/text()')
medalWinners=goldWinners+silverWinners+bronzeWinners

medalTotals={}
for name in medalWinners:
    if name in medalTotals:
        medalTotals[name]=medalTotals[name]+1
    else:
        medalTotals[name]=1

for result in sorted(medalTotals.items(), key=lambda x:x[1],reverse=True):
        print('%s:%s' % result)
