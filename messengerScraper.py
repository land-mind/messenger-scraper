from bs4 import BeautifulSoup
import os, csv

srcFolder = 'data'
outFile = 'scraped.csv'

def scrapePage(file):
	soup_page = BeautifulSoup(open(file), 'html.parser')
	thread = soup_page.find('div', attrs={'class' : 'thread'})
	metas = thread.find_all('div', attrs={'class' : 'message_header'})

	users = [meta.find('span', attrs={'class' : 'user'}, recursive=False).text for meta in metas]
	times = [meta.find('span', attrs={'class' : 'meta'}, recursive=False).text for meta in metas]
	msgs = [msg.text for msg in thread.find_all('p', recursive=False)]

def scrapeAll(folder):
	for file in os.listdir(folder):
	    if file.endswith('.html'):
	        scrapePage(os.path.join(folder, file)):

if __name__ == "__main__":
	scrapeAll('data')