import os
import json
import scrapy
from lxml import html
from datetime import date
from decimal import Decimal
balance_sheet_url = 'https://economictimes.indiatimes.com/hdfc-bank-ltd/balancesheet/companyid-{}.cms'
balance_sheet_output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data_collected/balance_sheet.txt')

class BalanceSheet(scrapy.Spider):
    name = 'balance_sheet'
    stock_names = ['hdfc_bank', 'axis_bank', 'indusind' ,'sbi', 'pnb', 'bob']
    company_ids = ['9195', '9175', '9196', '11984', '11585', '12040']
    allowed_domains = ['economictimes.indiatimes.com']
    start_urls = [balance_sheet_url.format(company_id) for company_id in company_ids]
    i = 0
    def parse(self, response):
        print(balance_sheet_output_file)
        output_file = open(balance_sheet_output_file, 'a')
        print("I value ---", self.i, BalanceSheet.i)
        print(self.start_urls[self.i])
        tree = html.fromstring(response.text)
        Data = tree.xpath('//td/text()')
        # BalanceSheet1 = tree.xpath('//td[@class="textR"]/text()')
        # print(Data)
        NetWorth = Data.index('Net Worth');  # print (NetWorth)
        SecuredLoan = Data.index('Secured Loan');
        TotalYears = SecuredLoan - NetWorth
        TotalLiabilities = Data.index('TOTAL LIABILITIES');  # print (TotalLiabilities)
        TotalCurrentAssests = Data.index('Total Current Assets');  # print (TotalCurrentAssests)
        TotalCurrentLiabilities = Data.index('Total Current Liabilities');  # print (TotalCurrentLiabilities)
        NETCURRENTASSETS = Data.index('NET CURRENT ASSETS');  # print (NETCURRENTASSETS)
        TOTALASSETS = Data.index('TOTAL ASSETS(A+B+C+D+E)');  # print (TOTALASSETS)

        # DATA = {'stock_name':self.stock_names[self.i],
        #  "Mar19": {'NetWorth': Data[NetWorth + 1], 'TotalLiabilities': Data[TotalLiabilities + 1],
        #            'TotalCurrentAssests': Data[TotalCurrentAssests + 1], 'NETCURRENTASSETS': Data[NETCURRENTASSETS + 1],
        #            'TOTALASSETS': Data[TOTALASSETS + 1]},
        #  "Mar18": {'NetWorth': Data[NetWorth + 2], 'TotalLiabilities': Data[TotalLiabilities + 2],
        #            'TotalCurrentAssests': Data[TotalCurrentAssests + 2], 'NETCURRENTASSETS': Data[NETCURRENTASSETS + 2],
        #            'TOTALASSETS': Data[TOTALASSETS + 2]},
        #  "Mar17": {'NetWorth': Data[NetWorth + 3], 'TotalLiabilities': Data[TotalLiabilities + 3],
        #            'TotalCurrentAssests': Data[TotalCurrentAssests + 3], 'NETCURRENTASSETS': Data[NETCURRENTASSETS + 3],
        #            'TOTALASSETS': Data[TOTALASSETS + 3]},
        #  "Mar16": {'NetWorth': Data[NetWorth + 4], 'TotalLiabilities': Data[TotalLiabilities + 4],
        #            'TotalCurrentAssests': Data[TotalCurrentAssests + 4], 'NETCURRENTASSETS': Data[NETCURRENTASSETS + 4],
        #            'TOTALASSETS': Data[TOTALASSETS + 4]},
        #  "Mar15": {'NetWorth': Data[NetWorth + 5], 'TotalLiabilities': Data[TotalLiabilities + 5],
        #            'TotalCurrentAssests': Data[TotalCurrentAssests + 5], 'NETCURRENTASSETS': Data[NETCURRENTASSETS + 5],
        #            'TOTALASSETS': Data[TOTALASSETS + 5]},
        #  }
        #
        # DATA_NEW = [{'year':'Mar19', 'stock_name':self.stock_names[self.i], 'NetWorth': Data[NetWorth + 1], 'TotalLiabilities': Data[TotalLiabilities + 1],
        #            'TotalCurrentAssests': Data[TotalCurrentAssests + 1], 'NETCURRENTASSETS': Data[NETCURRENTASSETS + 1],
        #            'TOTALASSETS': Data[TOTALASSETS + 1]
        #             }]
        years = ['2019-04-01','2018-04-01','2017-04-01','2016-04-01','2015-04-01',]

        detail_list = []
        for j in range(1,len(years)+1):
            detail = {
                'year':years[j-1],
                'stock_name':self.stock_names[self.i],
                'net_worth': Data[NetWorth + j],
                'total_liabilities' : Data[TotalLiabilities + j],
                'total_current_assests':Data[TotalCurrentAssests + j],
                'net_current_assets':Data[NETCURRENTASSETS + j],
                'total_assets':Data[TOTALASSETS + j]
            }
            detail_list.append(detail)
        output_file.write(str(detail_list))
        output_file.write('\n')

        print(detail_list)

        self.i += 1
        BalanceSheet.i += 1
        # print(DATA)

