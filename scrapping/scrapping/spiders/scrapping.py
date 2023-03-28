import scrapy

class TaskSpider(scrapy.Spider):
  name = 'task'
  start_urls = ['https://savollar.islom.uz/savollar?page=6600']

  
  def parse(self, response):
    
      for link in response.css('div.question a::attr(href)').getall():
        
        yield response.follow(link, callback=self.parse_task) 
      
      for i in range (6601, 7209):
        next_page = f'https://savollar.islom.uz/savollar?page={i}'
        yield response.follow(next_page, callback=self.parse)

        
  def parse_task(self, response):
    nlpdict={
        'section_info':response.css('ol a::text').getall()[1],
        'question_text':response.css('div.text_in_question').get().replace('<div class="text_in_question">',''),
        'answer_text':response.css('div.answer_in_question').get().replace('<div class="answer_in_question">',''),
        'views_info':response.css('div.info_quesiton').get().split()[-2],
        'date':response.css('div.info_quesiton::text').get().split()[2]

    }
    yield nlpdict