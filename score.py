
import re
import sys
import os

def usage():
    print('Usage:')
    print('\t{0} *.txt'.format(sys.argv[0]))

def read_txt(inputpath):
    li = list()
    with open(inputpath, "r") as f:
        line = f.readlines()
        for i in line:
            score=re.findall("Score=\d+", i)
            for j in score:
                li.append(re.findall(r"\d+\.?\d*",j))
    return li

if __name__ == "__main__":
    input_path = 'FurMark-Scores.txt'
    if len(sys.argv) == 2:
        txt = sys.argv[1]
        if os.path.exists(txt) & txt.endswith("txt"):
            print(read_txt(sys.argv[1]))
        else:
            print("input file is not a txt file")
    else:
        usage()