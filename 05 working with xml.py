import bs4 as bs
import urllib.request


# Sitemap Track with XML

source = urllib.request.urlopen("https://pythonprogramming.net/sitemap.xml").read()
soup = bs.BeautifulSoup(source, features='xml')

# print(soup)

for link in soup.find_all('loc'):
    print(link.text)