import requests
from bs4 import BeautifulSoup
import pandas as pd

def test():
    url = 'data/Unigine_Heaven_Benchmark_4.0_20220803_1402.html'
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
    return my_dict

def export_excel(export):
    # 将字典列表转换为DataFrame
    print("export=", export)
    pf = pd.DataFrame((list(export.items())))
    # 指定字段顺序
    order = export.keys()
    print("key_lis", list(order))
    pf = pf[order]
    # 指定生成的Excel表格名称
    file_path = pd.ExcelWriter('name.xlsx')
    # 替换空单元格
    pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False)
    # 保存表格
    file_path.save()


if __name__ == '__main__':
    mydict=test()
    export_excel(mydict)
