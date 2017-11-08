import requests
from bs4 import BeautifulSoup

class ScrapePage(object):
	def query(self, term):
		url = 'https://thepiratebay.org/search/suits' + term
		page = requests.request('GET', url)
		soup = BeautifulSoup(page.text, 'html.parser')

		item_holder = soup.find_all(class_='detName')
		item_anchor = item_holder.find_all('a')

		print( item_anchor )
