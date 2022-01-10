# indeed
--> create python virtual environment

--> pip install -r requirements.txt

--> scrapy crawl jobs -o la.csv

--> extracted skills results are in the skills.csv
--> crawling python scripts are in the folders. For instance: indeed_la > indeed_la > spiders > jobs.py

 # Conceptual Questions 1
## How do you scale your project to scrape all job postings daily from indeed?
 
   ### 1-- **define the traffic profile** 
      --Websites that you're trying to get data from, also if there's any technical challenges needed to be solved, like JS rendering.
      --Volume, meaning how many requests do you want to make per hour or per day. Also do you have any specific time window for the requests, like, for example you want to make           all your requests only during work hours, for some reason. Or is it okay to get the data at night, when there's significantly less traffic hitting the site.
      --Geo locations, because sometimes the website displays different content depending on where you are. So you need to use proxies that are in that specific region you need.
   ###   2-- **Proxy pool**
      -- How many proxies you will need
      -- Where those proxies should be located
      -- The type of the proxies (data center or residential)
   ### 3-- **Proxy Management**
      -- How many proxies you will need
      -- Where those proxies should be located
      -- The type of the proxies (data center or residential)
      
##  How many job postings are there in each of the locations given? How many of them can you scrape?
   ** **
    zip code 90013: 45,636 jobs
    zip code 10006: 272,494 jobs
    zip code 78714: 70,927 jobs
   
## How would you estimate the number of total jobs in the US? Is it possible to scrape this information from Indeed?
   according to each zip code, we can count total number of jobs. Yes, it is possible you have all zip codes in the US. 
   
# Conceptual Questions 2 
## Did you do any preprocessing or data cleaning on the job descriptions?
   ** **
    Yes, I did
## What are the shortcomings of this approach?
   ** ** 
    Sometimes you may lost meaningfull data because of data volume. If dataset is about specific domain such as economy or biology. You need to increase knowledge of these branches and need to consult the SME(subject matter expert).
## How would you improve the outcomes?
   ** **
    Adding new skills to the skill list may give more extracted skills. 
## (Optional) How would you use NLP to improve the result? (feel free to implement if you have time & resources)
   ** ** 
   NLP NER (Name Entity Recognition) enhances the result by Spacy etc. Thanks to NER rules, we can define the words structure (n-grams) then  matcher can identify the skills. 
   Ultimately, Regardless of which NLP algorithm you use, the most crucial thing is teh Data Quality, In order to get good results from the ML/DL algorithm. 
   



