from bs4 import BeautifulSoup
import urllib.request

url = 'https://data.nodc.noaa.gov/icoads/2010s/2010s'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)

soup = BeautifulSoup(resp, 'html.parser').find_all('a', href=True)


# Find all links containing Zone 1-4
# Use list comprehension
year = ['2015', '2016', '2017']
year_soup = [i for i in soup if any(z in i.get('href') for z in year)]


#Convert to Full Path
links = ['https://data.nodc.noaa.gov/icoads/2010s/2010s/' + i.get('href') for i in year_soup]

def length():
	print(len(links))

def get_links():
	return links


