import scrapy
class ArticleSpider(scrapy.Spider):
	name = "article"
	start_urls = ['https://goodk.at/lot1.html']
	def parse(self, response):
		content = response.xpath("//*[matches(@style,'left:6[0-9]{1}+.\d+px') and (@class='cls_002' or @class='cls_005')]").extract()
		price = response.xpath("//*[matches(@style,'left:5[0-9]{2}.\d+px') and (@class='cls_002' or @class='cls_005')]").extract()
		lot = response.xpath("//*[matches(@style,'left:[12345][0-9]{1}.\d+px') and (@class='cls_002' or @class='cls_005')]").extract()
		yield {'description': ''.join(content)} 
		yield {'prix': ''.join(price)}
		yield {'lot': ''.join(lot)}