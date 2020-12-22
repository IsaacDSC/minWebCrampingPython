# from urllib.request import urlopen
# html = urlopen('https://www.google.com/')
# #print(html.read())

#IDENTIFICANDO TECNOLOGIAS USADAS NO WEBSITE
# import builtwith
# resp = builtwith.parse('https://www.facebook.com/')
# print(resp)

# import whois
# domain = whois.query('google.com')
# print(domain.name)


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pypi.org/project/whois/')
bsObject = BeautifulSoup(html.read(), 'html.parser')

print(bsObject.h1)
print(bsObject.find_all('h2'))
for link in bsObject.find_all('a'):
    print(link)
    print(link.get('href'))
