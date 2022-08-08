import zipfile
import os.path
import sys
import tempfile
import shutil
from xml.etree import ElementTree 
import pandas
import win32file as pywin32

def get_xml(filename):
    if os.path.isfile(filename):
        name="Result.xml"
        tmp = tempfile.mkdtemp()
        zipfile.ZipFile(filename).extractall(tmp)
        shutil.copyfile(os.path.join(tmp,name), name)
        shutil.rmtree(tmp)
        return name
    else:
        print(filename, " is not a file")
        sys.exit(0)

def usage():
    if len(sys.argv) != 2:
        print("Usage\n\t", sys.argv[0], "filename")
        print("\t For example:", sys.argv[0], "test.3dmark-result'")
        sys.exit(0)

def parse_xml(xml):
    data=dict()
    dom = ElementTree.parse(xml)
    root = dom.getroot()
    result = root.findall(".//result/")
    for element in result:
        data[element.tag]=element.text
    return data

def save_excel(file,datas):
    if is_used(file) & os.path.exists(file):
        prefix,suffix = os.path.splitext(file)
        file = prefix + "_occupied" + suffix
        print("the file is occupied!!!")
    key=list(datas.keys())
    value=list(datas.values())
    p = pandas.DataFrame()
    p.fillna(' ', inplace=True)
    p["名称"]=key
    p["结果"]=value
    p.to_excel(file,encoding = 'utf-8',index = False)

def is_used(file_name):
	try:
		vHandle = pywin32.CreateFile(file_name, pywin32.GENERIC_READ, 0, None, pywin32.OPEN_EXISTING, pywin32.FILE_ATTRIBUTE_NORMAL, None)
		return int(vHandle) == pywin32.INVALID_HANDLE_VALUE
	except:
		return True
	finally:
		try:
			pywin32.CloseHandle(vHandle)
		except:
			pass

if __name__ == '__main__':
    usage()
    input=sys.argv[1]
    xml=get_xml(input)
    save_excel(os.path.join("data","3dmark_result.xlsx"), parse_xml(xml))