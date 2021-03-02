import scrapy
import time

class AmazonReviewSpider(scrapy.Spider):
    # Spider name
    name = 'amazon_review'

    # Domain names to scrape
    allowed_domains = ['amazon.com']

    # Base URL for reviews
    myBaseUrl = "https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy%E2%80%91/product-reviews/B07VGRJDFY/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
    start_urls = []

    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,500):
        start_urls.append(myBaseUrl+str(i))

    # Defining a Scrapy parser
    def parse(self, response):
        data = response.css('#cm_cr-review_list')

        # Collecting product star ratings
        star_rating = data.css('.review-rating')

        # Collecting user reviews
        comments = data.css('.review-text')
        count = 0

        # Combining the results
        for review in star_rating:
            yield{'stars': ''.join(review.xpath('.//text()').extract()),
                    'comment': ''.join(comments[count].xpath(".//text()").extract())
                    }
            count=count+1
