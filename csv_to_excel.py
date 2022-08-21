import os
import pandas as pd

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
    print(datas)
    datas.to_excel(excel_path,index=False)

if __name__ == '__main__':
    path="data"
    # 查看数据路径是否存在
    mk_dir(path)
    csv_file = 'pm_log.csv'
    excel_file = 'pm_log.xlsx'
    csv_path=os.path.join(path,csv_file)
    excel_path=os.path.join(path,excel_file)
    # mk_file(excel_path)
    cols=['Time Stamp','GPU0 Power Socket Power','GPU0 Power TCP Estimated Power']
    csv_excel(csv_path,excel_path,cols)
    # del_column(excel_path)

