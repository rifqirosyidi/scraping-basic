import bs4 as bs
import urllib.request
import pandas as pd

# source = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
# soup = bs.BeautifulSoup(source, features='lxml')


# In pandas if you read the html it will search the table data

dfs = pd.read_html("https://pythonprogramming.net/parsememcparseface/", header=0)  # remove first data / heading
for df in dfs:
    print(df)

# With this you can perform calculation more easily
