# from jobs import JobsSpider1
# import scrapy
#
#
# class JobsSpider(JobsSpider1):
#
#     # Rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="resultsCol"]/nav/div/ul/li[6]/a',)), callback="parse", follow=True),)
#
#     def __init__(self):
#         self.next_page_url = 'https://www.indeed.com/cmp/' + self.name
#         self.name = JobsSpider1().company_name
#
#     def parse(self):
#         name = 'ratings'
#         allowed_domains = ['indeed.com']
#         rate_url = [f'https://www.indeed.com/cmp/{self.name}']
#         yield  scrapy.Request(rate_url, callback=self.parse)
#
#     def parse_rate(self, response):
#         rate = response.xpath('//*[@id="cmp-container"]/div/div[1]/header/div[2]/div[3]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/span[2]/text()').extract_first()
#         yield {'rate':rate}