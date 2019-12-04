import bs4 as bs
import urllib.request


source = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup = bs.BeautifulSoup(source, 'lxml')

print(soup.find_all("p"))

for paragraph in soup.find_all("p"):
    print(paragraph.string)  # String Return None if it has child tag

for paragraph in soup.find_all('p'):
    print(paragraph.text)


# Get All The text
print(soup.getText())


# Get All The Url
for url in soup.find_all('a'):
    print(url.get('href'))
