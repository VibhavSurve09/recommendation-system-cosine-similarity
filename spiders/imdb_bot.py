import scrapy
from ..items import ImdbItem

class ImdbBotSpider(scrapy.Spider):
    name = 'imdb-bot'
    cnt=1
    start_urls = [
        "https://www.imdb.com/list/ls057823854/?sort=list_order,asc&st_dt=&mode=detail&page=1"
    ]

    def parse(self, response):
        movies=ImdbItem()
        all_movies=response.css(".mode-detail")
        for movie in all_movies:
            movieName=movie.css(".lister-item-header a").css("::text").extract()
            movieYear=movie.css(".text-muted.unbold::text").extract()
            movie_directors_cast=movie.css(".text-muted a").css("::text").extract()
            movieTime=movie.css(".runtime::text").extract()
            movieTags=movie.css(".genre::text").extract()
            movieStars=movie.css(".ipl-rating-star.small .ipl-rating-star__rating").css("::text").extract()
            movieScore=movie.css(".metascore::text").extract()
            movieDis=movie.css(".ratings-metascore+ p").css("::text").extract()
            movieVotes=movie.css(".text-muted+ span:nth-child(2)").css("::text").extract()
            movieTotal=movie.css(".ghost~ .text-muted+ span").css("::text").extract()
        
            movies["movie_name"]=movieName
            movies["movie_year"]=movieYear
            movies["movie_directors_cast"]=movie_directors_cast
            movies["movie_time"]=movieTime
            movies["movie_tags"]=movieTags
            movies["movie_stars"]=movieStars
            movies["movie_score"]=movieScore
            movies["movie_dis"]=movieDis
            movies["movie_votes"]=movieVotes
            movies["movie_total"]=movieTotal

            yield movies
        ImdbBotSpider.cnt+=1
        if ImdbBotSpider.cnt<101:
            next_page="https://www.imdb.com/list/ls057823854/?sort=list_order,asc&st_dt=&mode=detail&page="+str(ImdbBotSpider.cnt)
            yield response.follow(next_page,self.parse)


