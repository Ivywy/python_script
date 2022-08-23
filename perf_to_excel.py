
import re
import sys
import os
from xml.etree import ElementTree
from util import common

from bs4 import BeautifulSoup


def read_txt(inputpath,app):
    li = list()
    dic={}
    with open(inputpath, "r") as f:
        line = f.readlines()
        for i in line:
            score=re.findall("Score=\d+", i)    # ['Score=505']
            # print("score",score)
            for j in score:
                li.append(re.findall(r"\d+\.?\d*",j))   # [['505']]
                # print("li",li)
    dic[app]=li[0][0]    # 只抽取第一个score
    return dic

def read_html(file_path,app):
    doc = open(file_path, 'r', encoding='utf-8').read()
    soup = BeautifulSoup(doc, "html.parser")
    total=soup.findAll(text=re.compile('.*?Total.*?'))
    # print(total)
    s=""
    dic={}
    for str in total:
        if str.find("Total scores")!=-1:
            s=str.split("Total scores: ")[1]
            break
    dic[app]=float(s)
    return dic

            # for s in re.findall(r'-?\d+\.?\d*', str):
            #     print(s)
def read_xml(file_path,app,item):
    data=dict()
    dom = ElementTree.parse(file_path)
    root = dom.getroot()
    # print(root)
    result = root.findall(".//result/")
    # print(result)
    for element in result:
        # print(element.tag)
        # print("===============")
        # data[element.tag]=element.text
        if element.tag == item:
            data[app] = element.text
            break
    return data

if __name__ == "__main__":

    data_path="data"

    # 读取Furmark的score
    furmark_path=os.path.join(data_path,"FurMark-Scores.txt")
    print(read_txt(furmark_path,"Furmark"))

    # 读取heaven11的score
    heaven_path=os.path.join(data_path,"heaven11_log.html")
    print(read_html(heaven_path,"heaven11"))

    # 读取Firestrike的数据
    firestrike_path=os.path.join(data_path,"Result-Firestrike.xml")
    print(read_xml(firestrike_path,"FireStrike","FireStrikeCustomGraphicsScore"))

    # 读取timespy的数据
    timespy_path=os.path.join(data_path,"Result-TimespyExtreme.xml")
    print(read_xml(timespy_path,"TimeSpy","TimeSpyExtremeCustomGraphicsScore"))

    # 读取3Dmark11的数据
    file_3Dmark11=os.path.join(data_path,"3Dmark11.xml")
    print(read_xml(file_3Dmark11,"3Dmark11","graphicsscore"))






