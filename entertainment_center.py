import fresh_tomatoes, media
from lxml import html
import requests

# Scraping data from IMDB
class Imdb():
	def __init__(self, url, trailer):
		self.url = url
		self.trailer = trailer

	def page_tree(self): #  getting data from the HTML 
		page = requests.get(self.url)
		tree = html.fromstring(page.content)
		return tree

	def title(self): # getting the title
		tree = self.page_tree()
		title = tree.xpath("//h1[@itemprop='name']/text()")[0].encode('ascii','ignore').decode('ascii')
		return title
	
	def duration(self): # getting the duration from the data
		tree = self.page_tree()
		duration = tree.xpath("//time[@itemprop='duration']/text()")[1].encode('ascii','ignore').decode('ascii')
		return duration
	
	def movie_storyline(self): # storyline 
		tree = self.page_tree()
		movie_storyline = tree.xpath("//div[@class='summary_text']/text()")[0].encode('ascii','ignore').decode('ascii')
		return movie_storyline

	def poster_image(self): #  poster image
		tree = self.page_tree()
		poster_image = tree.xpath("//img/@src")[2].encode('ascii','ignore').decode('ascii')
		return poster_image

# Movies that are chosen
galaxy = Imdb('http://www.imdb.com/title/tt2015381', 
				'https://www.youtube.com/watch?v=89yh3vYs-zo')

indignation = Imdb('http://www.imdb.com/title/tt4193394',
					'https://www.youtube.com/watch?v=ELKsrUssyQE')

avatar = Imdb('http://www.imdb.com/title/tt0499549/?ref_=fn_al_tt_1',
				'https://www.youtube.com/watch?v=d1_JBMrrYw8')

galaxy_site = media.Movie(galaxy.title(), 
						galaxy.duration(),
						galaxy.movie_storyline(), 
						galaxy.poster_image(), 
						galaxy.trailer)

indignation_site = media.Movie(galaxy.title(), 
						indignation.duration(),
						indignation.movie_storyline(), 
						indignation.poster_image(), 
						indignation.trailer)

avatar_site = media.Movie(avatar.title(), 
						avatar.duration(),
						avatar.movie_storyline(), 
						avatar.poster_image(), 
						avatar.trailer)


movies = [galaxy_site, indignation_site, avatar_site]

fresh_tomatoes.open_movies_page(movies)

