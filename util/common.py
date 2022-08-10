import os
def mk_dir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("---  create new folder success...  ---")
    else:
        print ("---  There is this folder!  --")

def mk_file(pah_file):
    (path,file)=os.path.split(pah_file)
    print(path)
    print("==========")
    print(file)
    is_file=os.path.isfile(file)
    if not is_file:
        open(file,"wa+")
    os.chmod(file, stat.S_IWOTH|stat.S_IROTH)