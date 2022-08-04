import requests
from bs4 import BeautifulSoup

def test():
    url = 'Unigine_Heaven_Benchmark_4.0_20220803_1402.html'
    doc = open(url, 'r', encoding='utf-8').read()
    soup = BeautifulSoup(doc, "html.parser")
    # print("allText:",soup.findAll("table"))
    my_dict=dict()
    for table in soup.findAll("table"):
        for row in table.findAll('tr'):
            my_dict[row.find('td').string]=row.find('td').find_next().string
            # print(row.find('td').string)
            # print(row.find('td').find_next().string)

    print(my_dict)


if __name__ == '__main__':
    test()