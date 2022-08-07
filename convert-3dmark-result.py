import zipfile
import os.path
import sys
import tempfile
import shutil

def parsefile(filename):
    if os.path.isfile(filename):
        name="Result.xml"
        tmp = tempfile.mkdtemp()
        zipfile.ZipFile(filename).extractall(tmp)
        shutil.copyfile(os.path.join(tmp,name), name)
        shutil.rmtree(tmp)
    else:
        print(filename, " is not a file")


def usage():
    if len(sys.argv) != 2:
        print("Usage\n\t", sys.argv[0], "filename")
        print("\t For example:", sys.argv[0], "test.3dmark-result'")
        sys.exit(0)

if __name__ == '__main__':
    usage()
    file=sys.argv[1]
    parsefile(file)