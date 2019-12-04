import bs4 as bs
import urllib.request

source = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup = bs.BeautifulSoup(source, features='lxml')


# table = soup.table
table = soup.find('table')

print(table)
