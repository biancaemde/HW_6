import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

c = ssl.create_default_context()
c.check_hostname = False
c.verify_mode = ssl.CERT_NONE

url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Taylar.html', context=c).read()

names = []

for i in range (0, 7):
    soup = BeautifulSoup(url, 'html.parser')
    tags = soup('a')
    for j in range(1, len(tags)):
        if j == 17:
            url = urllib.request.urlopen(tags[j].get('href', None), context=c).read()
            names.append(tags[j].get('href', None))
print (names[6])