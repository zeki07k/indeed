import re
from datetime import datetime
import scrapy



class JobsSpider1(scrapy.Spider):
    start = datetime.now()
    name = 'jobs'
    allowed_domains = ['indeed.com']
    start_urls = ['https://www.indeed.com/jobs?q&l=New%20York%2C%20NY%2010006&radius=3&fromage=3&vjk=bbfaee5c3234326a']
    base_url = 'https://www.indeed.com/viewjob?jk='
    next_url = 'https://www.indeed.com/'
    # rate_url = 'https://www.indeed.com/cmp/Northwell-Health'

    # Rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="resultsCol"]/nav/div/ul/li[6]/a',)), callback="parse", follow=True),)


    def parse(self, response, **kwargs):
        global next_page_url
        jks = response.css('#mosaic-provider-jobcards a::attr(data-jk)').extract()
        for jk in jks:
            job_url = self.base_url + jk
            yield scrapy.Request(job_url, callback=self.parse_job)

        next_page_partial_url = response.css('#resultsCol > nav > div > ul > li:nth-child(6) > a::attr(href)').extract_first()
        print("URL", next_page_partial_url)

        next_page_url = self.next_url + next_page_partial_url

        yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_job(self, response):

        company_name = response.css('.jobsearch-CompanyReview--heading::text').extract_first()

        jk = re.sub('[^\s.](?:[^?.]|\.(?! ))*\?', '', response.request.url)
        date = response.css('.jobsearch-JobMetadataFooter > *:nth-child(2)::text').extract_first()
        job_text = response.css('#jobDescriptionText').extract_first()
        job_description = re.sub('<[^<]+?>', '', job_text)

        try:
            job_type = response.css('.jobsearch-JobDescriptionSection-sectionItem>div::text').getall()[1]
        except:
            job_type = response.css('.jobsearch-JobDescriptionSection-sectionItem>div::text').extract_first()

        job_title = response.css('.jobsearch-JobInfoHeader-title-container>h1::text').getall()[0]

        try:
            job_location = response.css('.jobsearch-jobLocationHeader-location::text').get().split(',')[2].split(' ')
        except:
            job_location = None

        salary = response.css('.jobsearch-JobDescriptionSection-sectionItem>span::text').extract_first()

        try:
            state = response.css('.jobsearch-jobLocationHeader-location::text').get().split(',')[2].split(' ')
        except:
            state = None

        try:
            zip_code = response.css('.jobsearch-jobLocationHeader-location::text').extract_first().split(',')[2].split(' ')[2]
        except:
            zip_code = None

        url = response.request.url
        finish = datetime.now()
        time = finish - self.start

        yield {
               'company': company_name,
               'jk': jk,
               'posting_date': date,
               'job_description': job_description,
               'job_type': job_type,
               'job_title': job_title,
               'job_location': job_location,
               'salary': salary,
               'state': state,
               'zip_code': zip_code,
               'scrape_time': time,
               'url': url
              }
