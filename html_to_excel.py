import os

from util import common
from bs4 import BeautifulSoup
import pandas as pd

def html_excel(src_html,des_excel):
    # 从html中提取数据
    doc = open(src_html, 'r', encoding='utf-8').read()
    soup = BeautifulSoup(doc, "html.parser")
    # print("allText:",soup.findAll("table"))
    my_dict=dict()
    for table in soup.findAll("table"):
        for row in table.findAll('tr'):
            my_dict[row.find('td').string]=row.find('td').find_next().string
            # print(row.find('td').string)
            # print(row.find('td').find_next().string)

    print(my_dict)

    # 将数据输出到excel
    lis=list()
    lis.append(my_dict)
    pd.DataFrame(lis).to_excel(des_excel, index=False)

if __name__ == '__main__':
    path="data"
    # 查看数据路径是否存在
    common.mk_dir(path)
    html_file = 'Unigine_Heaven_Benchmark_4.0_20220803_1402.html'
    excel_file='output2.xlsx'
    html_path=os.path.join(path,html_file)
    excel_path=os.path.join(path,excel_file)
    html_excel(html_path,excel_path)
