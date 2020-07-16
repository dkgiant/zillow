# -*- coding: utf-8 -*-
import scrapy


class ZillowHousesSpider(scrapy.Spider):
    name = 'zillow_houses'
    allowed_domains = ['www.zillow.com']
    start_urls = ['http://www.zillow.com/']

    def parse(self, response):
        pass
