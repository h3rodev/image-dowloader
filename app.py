#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
from random import randint
import datetime
import time
from time import sleep

i = datetime.datetime.now()
def getProductLinks(q,c):

	sleep( randint(0, 1) )
	url = "https://www.pexels.com/search/"+q+"?page="+c+"&seed="+str( i )
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data, "html.parser")

	links = []

	for link in soup.find_all('img'):
		src = str( link.get('src') ).replace('-medium.jpg','.jpg')

		if src:
			if 'https://static.pexels.com/photos/' in src:
				if not src in links:
					links.append(src)

	return links

def getAllImgUrl(q):
	sleep( randint(0, 1) )
	c = 1
	urlList = []
	while getProductLinks(q,str(c) ):
		urlList.append( getProductLinks(q,str(c) ) )
		c = c + 1

	return str( urlList ).replace('[','').replace(']','').replace("'","").replace(","," ").split()

category = raw_input("Search Images? ")

for url in getAllImgUrl(category):
	sleep( randint(0, 1) )
	fileName = str( int(time.time()) )+"-"+str( url.split('/')[5] )
	print fileName
	directory = 'path to directory'
	response = requests.get(url, stream=True)
	if response.status_code == 200:
		if not 'medium' in url:
		    f = open(directory+fileName, 'wb')
		    print "Saving " + fileName + " on location " + directory
		    f.write(response.content)
		    f.close()
		    print "Done Saving The File " + fileName
	    



