from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.ncei.noaa.gov/thredds/catalog/OisstBase/NetCDF/AVHRR/catalog.html'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)

soup = BeautifulSoup(resp, 'html.parser').find_all('a', href=True)


# Find all links containing 2015-2017
# Use list comprehension
year = ['2015', '2016', '2017']
year_soup = [i for i in soup if any(z in i.get('href') for z in year)]

sub_links=[]

for link_year in year_soup:
	url = "https://www.ncei.noaa.gov/thredds/catalog/OisstBase/NetCDF/AVHRR/" + link_year.get('href')
	req = urllib.request.Request(url)
	resp = urllib.request.urlopen(req)
	soup = BeautifulSoup(resp, 'html.parser').find_all('a', href=True)

	#Find all sublinks containing 2015-2017
	year_soup2 = [i for i in soup if any(z in i.get('href') for z in year) and '.nc' in i.get('href')]
		
	#Convert to Full Path
	for link_year2 in year_soup2:
		sub_links.append(url.rstrip('catalog.html') + link_year2.get('href'))

links = []
for sub_link in sub_links:
	print(sub_link)
	url = sub_link
	req = urllib.request.Request(url)
	resp = urllib.request.urlopen(req)
	soup = BeautifulSoup(resp, 'html.parser').find_all('a', href=True)

	#Link must contain 'fileServer'
	filtered_soup = [i for i in soup if 'fileServer' in i.get('href')]
	for filtered_link in filtered_soup:
		links.append("https://www.ncei.noaa.gov/" + filtered_link.get('href'))

def length():
	print(len(links))

def get_links():
	return links


