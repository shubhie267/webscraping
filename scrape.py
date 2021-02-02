import requests
from bs4 import BeautifulSoup
import pprint #importing module pretty print

res = requests.get('https://news.ycombinator.com/news') #res is variable i.e. response

#print(res.text) 	#this gives you whole html page of the URL.

soup = BeautifulSoup(res.text , 'html.parser') #we mentioned html bcz it also parses xml files
links = soup.select('.storylink')   #grabbing all the links
subtext = soup.select('.subtext')
	#grabbing all the votes
#print(soup.body) 		#we will get the body part of html file
#print(soup.find_all('div'))
#print(soup.find_all('a')) 		#get all links
#print(soup.a)		or soup.find(a)			#get first link
#print(soup.title)				#get the title of website

# print(soup.find(id='score_25928310')) #gives you the points here output i got is 385 points

def create_custom_hn(links, subtext):
	hn = []   #list
	for index, item in enumerate(links):
		title = links[index].getText()
		href = links[index].get('href', None)
		vote = subtext[index].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points',''))
			if points > 99:
				print(points)
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})
	return hn
   
pprint.pprint(create_custom_hn(links, subtext))		#using pprint instaed of print

