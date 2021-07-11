# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    movie_year=scrapy.Field()
    movie_directors_cast=scrapy.Field()
    movie_time=scrapy.Field()
    movie_tags=scrapy.Field()
    movie_stars=scrapy.Field()
    movie_score=scrapy.Field()
    movie_dis=scrapy.Field()
    movie_votes=scrapy.Field()
    movie_total=scrapy.Field()
    
