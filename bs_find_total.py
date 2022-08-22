import string
from bs4 import BeautifulSoup
import re

def test():
    url = 'log20220819163656.html'
    doc = open(url, 'r', encoding='utf-8').read()
    soup = BeautifulSoup(doc, "html.parser")

    total=soup.findAll(text=re.compile('.*?Total.*?'));
    for t in total:
        print(t);



if __name__ == '__main__':
    test();