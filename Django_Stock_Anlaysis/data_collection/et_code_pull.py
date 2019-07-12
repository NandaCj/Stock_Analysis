import requests
import re
from lxml import html
url = 'https://economictimes.indiatimes.com/marketstats/company-true,exchange-50,indexid-1913,indexname-Nifty%2520Bank,marketcap-largecap%252Cmidcap,pageno-1,pid-38,sortby-percentChange,sortorder-desc.cms'
response = requests.get(url)
# print(response.text)
tree = html.fromstring(response.text)
links = re.findall('Pos_1_https(.*)cms', response.text)

print(links)



# print(tree.xpath("//a/"))
# Data = tree.xpath('//td/text()')
# print(Data)