import pandas as pd
from bs4 import BeautifulSoup
import codecs
import markdown
import io
file = input("Имя файла:")
html = codecs.open(file+".html","r",'utf-8')
soup = BeautifulSoup(html.read(),'lxml')
table = soup.find_all('table')[11]
table.select('tr')
table.extract()
with io.open(file+'.md', "a", encoding="utf-8") as f:
    f.write(markdown.markdown(str(table),extensions=['tables']))