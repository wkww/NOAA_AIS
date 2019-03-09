from bs4 import BeautifulSoup
import urllib.request

# url = 'https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2009/index.html'
url = 'https://marinecadastre.gov/ais/'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)

soup = BeautifulSoup(resp, 'html.parser').find_all('a', href=True)


# Find all links containing 2015-2017
# Use list comprehension
zone = ['Zone1_', 'Zone2_', 'Zone3_','Zone4_']
year = ['2015', '2016', '2017']
year_soup = [i for i in soup if any(z in i.get('href') for z in year)]

links = []

for link_year in year_soup:

	url = link_year.get('href')
	req = urllib.request.Request(url)
	resp = urllib.request.urlopen(req)

	soup = BeautifulSoup(resp, 'html.parser').find_all('a', href=True)

	#Find all links containing Zone1-4
	zone = ['Zone1_', 'Zone2_', 'Zone3_','Zone4_', 'Zone01', 'Zone02', 'Zone03', 'Zone04']
	zone_soup = [i for i in soup if any(z in i.get('href') for z in zone)]

	#Convert to Full Path
	for link_zone in zone_soup:
		links.append(link_year.get('href').rstrip('index.html') + link_zone.get('href'))

def length():
	print(len(links))

def get_links():
	return links


