from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
from pprint import pprint

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

values = []
tags = soup.find_all('span')
for tag in tags:
	values.append(int(tag.string))
sums = sum(values)

print ("Count:" + str(len(values)))
print ("Sum:" + str(sums))