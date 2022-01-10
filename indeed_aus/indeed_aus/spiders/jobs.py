import re
from datetime import datetime
import scrapy


class JobsSpider(scrapy.Spider):
    start = datetime.now()
    name = 'jobs'
    allowed_domains = ['indeed.com']
    start_urls = [
        'https://www.indeed.com/jobs?as_and&as_phr&as_any&as_not=gigs&as_ttl&as_cmp&jt=all&st&salary&radius=6&l=90013&fromage=any&limit=10&sort&psf=advsrch&from=advancedsearch&vjk=dc10e196e15b8da0',
        'https://www.indeed.com/cmp/']
    base_url = 'https://www.indeed.com/viewjob?jk='
    next_url = 'https://www.indeed.com/'
    rate_url = 'https://www.indeed.com/cmp/'

    def parse(self, response, **kwargs):

        next_page_partial_url = response.css('#resultsCol > nav > div > ul > li:nth-child(6) > a::attr(href)').extract_first()

        jks = response.css('#mosaic-provider-jobcards a::attr(data-jk)').extract()
        counter=0
        for jk in jks:
            job_url = self.base_url + jk
            yield scrapy.Request(job_url, callback=self.parse_job)
            try:
                try:
                    self.company_name = response.css('.jobsearch-CompanyReview--heading::text').extract_first()
                    yield scrapy.Request(self.rate_url + f'{self.company_name}', callback=self.parse_rate)
                except:
                    name = response.css('a::text').extract()[42]
                    self.company_name = re.sub('[A-Za-z]+', '', name)
                for name in self.company_name:
                    yield scrapy.Request(self.rate_url + f'{name}', callback=self.parse_rate)
            except:
                pass
            counter += 1
            if counter==200:
                break


        next_page_url = self.next_url + next_page_partial_url
        yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_rate(self, response):
        for i in response.css('span::text').extract():
            if i.endswith('stars.'):
                self.rate = i[:4]
                return self.rate

    def parse_job(self, response):

        self.company_name = response.css('.jobsearch-CompanyReview--heading::text').extract_first()

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
            zip_code = \
            response.css('.jobsearch-jobLocationHeader-location::text').extract_first().split(',')[2].split(' ')[2]
        except:
            zip_code = None

        url = response.request.url
        finish = datetime.now()
        time = finish - self.start
        print("RT", self.rate)
        yield {
            'company': self.company_name,
            'jk': jk,
            'posting_date': date,
            'job_description': job_description,
            'job_type': job_type,
            'job_title': job_title,
            'job_location': job_location,
            'rate': self.rate,
            'salary': salary,
            'state': state,
            'zip_code': zip_code,
            'scrape_time': time,
            'url': url
        }
