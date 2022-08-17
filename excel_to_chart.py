import os

import pandas as pd
import matplotlib.pyplot as plt

def excel_to_chart(path_file):
    df = pd.read_excel(path_file)
    ind=df.columns.tolist() #获取表头

    for i in range(1, len(ind)):
        plt.plot(df[ind[0]], df[ind[i]], label=ind[i])
    plt.xlabel(ind[0])
    plt.ylabel('Power')
    plt.title("summy of input")
    plt.legend()
    plt.grid()
    # plt.show()
    plt.savefig(r'data\pm_log.png')
if __name__ == '__main__':
    path="data"
    # mk_dir(path)
    excel_file = 'pm_log.xlsx'
    excel_path=os.path.join(path,excel_file)
    excel_to_chart(excel_path)
