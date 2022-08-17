import os
import pandas as pd
import xlwt
import xlrd
from xlutils.copy import copy
from util.common import mk_dir


def del_column(path_file):
    df=pd.read_excel(path_file)
    # df = pd.DataFrame(np.arange(12).reshape(3, 4))
    print("++++++++++++++")
    print(df)
    # df.drop(columns='Unnamed: 0',inplace=True)
    df = df[df.columns.drop(list(df.filter(regex='Unnamed')))]
    # print(df)

def csv_excel(csv_path,excel_path,columns):
    file = pd.read_csv(csv_path)
    datas=file[columns]
    print("++++++++++++++")
    # print(datas)
    # 求最大值和平均值并写入excel
    max_lis=list()
    max_lis.append("Max")
    aver_lis=list()
    aver_lis.append("Average")
    value_title=datas.columns.tolist()
    value_title[0]="value_type"
    title_lis=list()
    title_lis.append(value_title)
    print("excel_lis=",title_lis)
    print("value_title=",title_lis[0])
    write_excel_xls(excel_path,"sheet_1",title_lis)
    for i in columns[1:]:
        max_value=file[i].max()
        # print(max_value)
        max_lis.append(max_value)
        aver_value=file[i].mean()
        # print(aver_value)
        aver_lis.append(aver_value)
    print("max_lis=",max_lis)
    print("aver_lis=",aver_lis)
    value_lis=list()
    value_lis.append(max_lis)
    value_lis.append(aver_lis)
    write_excel_xls_append(excel_path,value_lis)
    # datas.to_excel(excel_path,index=False)

def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")


def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    print("xls格式表格【追加】写入数据成功！")


def read_excel_xls(path):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    for i in range(0, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            print(worksheet.cell_value(i, j), "\t", end="")  # 逐行逐列读取数据
        print()

if __name__ == '__main__':
    path="data"
    # 查看数据路径是否存在
    mk_dir(path)
    csv_file = 'pm_log.csv'
    excel_file = 'pm_log.xls'
    csv_path=os.path.join(path,csv_file)
    excel_path=os.path.join(path,excel_file)
    # mk_file(excel_path)
    cols=['Time Stamp','GPU0 Power Socket Power','GPU0 Frequencies Target Frequency GFXCLK','GPU0 Frequencies Actual Frequency GFXCLK','GPU0 Power TGP Power','GPU0 Temperature Hotspot','GPU0 Temperature MEM','GPU0 Fan PWM']
    csv_excel(csv_path,excel_path,cols)
    # del_column(excel_path)
