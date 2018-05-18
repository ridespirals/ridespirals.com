#
# Download all images used in the Wellness Guide
#
# http://members.shaw.ca/stevejobber/doug/images/

from bs4 import BeautifulSoup
import urllib, urllib2

url_root = 'http://members.shaw.ca/stevejobber/doug/images/'
page_contents = urllib2.urlopen(url_root).read()

soup = BeautifulSoup(page_contents)

for link in soup.find_all('a'):
	file_name = link.get('href')
	if '.png' in file_name:		
		image_url = url_root + file_name
		
		print('Trying: ', image_url)

		urllib.urlretrieve(image_url, './images/' + file_name)