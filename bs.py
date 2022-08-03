import requests
from bs4 import BeautifulSoup

def main():
    url = 'Unigine_Heaven_Benchmark_4.0_20220803_1402.html'
    doc = open(url, 'r', encoding='utf-8').read()
    soup = BeautifulSoup(doc, "html.parser")

    for table in soup.findAll("table"):
        for row in table.findAll('tr'):
            print(row.find('td').string)
            print(row.find('td').find_next().string)


main()