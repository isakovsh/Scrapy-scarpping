import scrapy

class TaskSpider(scrapy.Spider):
  name = 'task'
  start_urls = ['https://it-park.uz/ru/itpark/news/']

  
  def parse(self, response):
    
      for link in response.css('a.article-card::attr(href)').getall():
        
        yield response.follow(link, callback=self.parse_task) 
      
      for i in range (1, 3):
        next_page = f'https://it-park.uz/ru/itpark/news?page={i}'
        yield response.follow(next_page, callback=self.parse)

        
  def parse_task(self, response):
    taskdict={
      'title':response.css('h5::text').get(),
      'all_text':" ".join(response.css('span::text').getall()[1:]).replace(' ',''),
      'day':response.css('div.text-right p::text').get()
    }
    yield taskdict