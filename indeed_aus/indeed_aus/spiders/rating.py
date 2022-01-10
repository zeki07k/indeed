#
# class JobsSpider(scrapy.Spider):
#     start = datetime.now()
#     name = 'jobs'
#     allowed_domains = ['indeed.com']
#     start_urls = ['https://www.indeed.com/jobs?as_and&as_phr&as_any&as_not=gigs&as_ttl&as_cmp&jt=all&st&salary&radius=3&l=90013&fromage=any&limit=10&sort&psf=advsrch&from=advancedsearch&vjk=dc10e196e15b8da0']
#     base_url = 'https://www.indeed.com/viewjob?jk='
#     next_url = 'https://www.indeed.com/'
#     # rate_url = 'https://www.indeed.com/cmp/Northwell-Health'
#
#     # Rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="resultsCol"]/nav/div/ul/li[6]/a',)), callback="parse", follow=True),)
#
#
#     def parse(self, response, **kwargs):
#         global next_page_url
#         jks = response.css('#mosaic-provider-jobcards a::attr(data-jk)').extract()
#         for jk in jks:
#             job_url = self.base_url + jk
#             print("jb", job_url)
#             yield scrapy.Request(job_url, callback=self.parse_job)
#
#         next_page_partial_url = response.css('#resultsCol > nav > div > ul > li:nth-child(6) > a::attr(href)').extract_first()
#         print("URL", next_page_partial_url)
#
#         next_page_url = self.next_url + next_page_partial_url
#         yield scrapy.Request(next_page_url, callback=self.parse)
#
#
#     def parse_job(self, response):
#
#
#
#
#
#
#
#         yield {
#
#
#         }
