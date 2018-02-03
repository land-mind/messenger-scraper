from bs4 import BeautifulSoup
import os, csv

srcFolder = 'data'
outFile = 'scraped.csv'

def scrapePage(fname):
	pass

def scrapeAll(folder):
	for file in os.listdir(folder):
	    if file.endswith('.html'):
	        scrapePage(os.path.join(folder, file))

if __name__ == "__main__":
	print(scrapeAll('data'))