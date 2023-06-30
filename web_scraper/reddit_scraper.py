```python
import scrapy
from scrapy.crawler import CrawlerProcess
from web_scraper.spiders.reddit_spider import RedditSpider
from web_scraper.items import RedditScraperItem
from web_scraper.pipelines import JSONExportPipeline

class RedditScraper:
    def __init__(self):
        self.process = CrawlerProcess(settings={
            'ITEM_PIPELINES': {'web_scraper.pipelines.JSONExportPipeline': 1},
            'FEED_FORMAT': 'json',
            'FEED_URI': 'output.json'
        })

    def run_spider(self, subreddit):
        self.process.crawl(RedditSpider, subreddit=subreddit)
        self.process.start()

if __name__ == "__main__":
    scraper = RedditScraper()
    scraper.run_spider('python')
```
This script initiates the Scrapy process, sets the pipeline to JSONExportPipeline, and sets the output file to 'output.json'. It then starts the RedditSpider with a specified subreddit ('python' in this case).