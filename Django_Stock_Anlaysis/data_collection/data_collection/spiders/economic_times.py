import scrapy
from lxml import html

class BalanceSheet(scrapy.Spider):
    name = 'balance_sheet'
    allowed_domains = ['economictimes.indiatimes.com']
    start_urls = ['https://economictimes.indiatimes.com/hdfc-bank-ltd/balancesheet/companyid-9195.cms']

    def parse(self, response):
        tree = html.fromstring(response.text)
        Data = tree.xpath('//td/text()')
        # BalanceSheet1 = tree.xpath('//td[@class="textR"]/text()')
        print(Data)
        NetWorth = Data.index('Net Worth');  # print (NetWorth)
        SecuredLoan = Data.index('Secured Loan');
        TotalYears = SecuredLoan - NetWorth
        TotalLiabilities = Data.index('TOTAL LIABILITIES');  # print (TotalLiabilities)
        TotalCurrentAssests = Data.index('Total Current Assets');  # print (TotalCurrentAssests)
        TotalCurrentLiabilities = Data.index('Total Current Liabilities');  # print (TotalCurrentLiabilities)
        NETCURRENTASSETS = Data.index('NET CURRENT ASSETS');  # print (NETCURRENTASSETS)
        TOTALASSETS = Data.index('TOTAL ASSETS(A+B+C+D+E)');  # print (TOTALASSETS)

        DATA = {
         "Mar19": {'NetWorth': Data[NetWorth + 1], 'TotalLiabilities': Data[TotalLiabilities + 1],
                   'TotalCurrentAssests': Data[TotalCurrentAssests + 1], 'NETCURRENTASSETS': Data[NETCURRENTASSETS + 1],
                   'TOTALASSETS': Data[TOTALASSETS + 1]},
         "Mar18": {'NetWorth': Data[NetWorth + 2], 'TotalLiabilities': Data[TotalLiabilities + 2],
                   'TotalCurrentAssests': Data[TotalCurrentAssests + 2], 'NETCURRENTASSETS': Data[NETCURRENTASSETS + 2],
                   'TOTALASSETS': Data[TOTALASSETS + 2]},
         "Mar17": {'NetWorth': Data[NetWorth + 3], 'TotalLiabilities': Data[TotalLiabilities + 3],
                   'TotalCurrentAssests': Data[TotalCurrentAssests + 3], 'NETCURRENTASSETS': Data[NETCURRENTASSETS + 3],
                   'TOTALASSETS': Data[TOTALASSETS + 3]},
         "Mar16": {'NetWorth': Data[NetWorth + 4], 'TotalLiabilities': Data[TotalLiabilities + 4],
                   'TotalCurrentAssests': Data[TotalCurrentAssests + 4], 'NETCURRENTASSETS': Data[NETCURRENTASSETS + 4],
                   'TOTALASSETS': Data[TOTALASSETS + 4]},
         "Mar15": {'NetWorth': Data[NetWorth + 5], 'TotalLiabilities': Data[TotalLiabilities + 5],
                   'TotalCurrentAssests': Data[TotalCurrentAssests + 5], 'NETCURRENTASSETS': Data[NETCURRENTASSETS + 5],
                   'TOTALASSETS': Data[TOTALASSETS + 5]},
         }

        print(DATA)
