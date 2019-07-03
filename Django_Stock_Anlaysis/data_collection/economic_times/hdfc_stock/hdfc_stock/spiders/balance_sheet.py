# -*- coding: utf-8 -*-
import scrapy


class BalanceSheetSpider(scrapy.Spider):
    name = 'balance_sheet'
    allowed_domains = ['https://economictimes.indiatimes.com/']
    start_urls = ['https://economictimes.indiatimes.com/hdfc-bank-ltd/balancesheet/companyid-9195.cms']

    def parse(self, response):
        print(response.text)
        yield response.text
