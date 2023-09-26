# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
import time
# path_list = []
# file_list = []
path1 = os.path.join(os.path.expanduser("~"), 'Desktop')+"/EOSI"
path2 = os.path.join(os.path.expanduser("~"), 'Desktop')+"/EOSI_Tests"
print(path1)
total = 0
# def f(path):
#     global total
#     for home, dirs, files in os.walk(path):
#         if len(files) :
#             for file in files:
#                 if file.count(".h") or file.count(".cpp") :
#                         if not file.count("sqlite3") and not file.count("qcustomplot") and not file.count("plotexamples"):
#                             p = os.path.join(home,file)
#                             if file_list.count(p):
#                                 continue
#                             file_list.append(p)
#                             print("file = ",p)
#                             count = len(open(p, 'r',encoding="utf-8").readlines())
#                             total += count
#                             #print(p,count)

#         if len(dirs):
#             for dir in dirs:
#                 d = os.path.join(home,dir)
#                 if path_list.count(d) or d.count(".git") or d.count("qtDeployDll") \
#                     or d.count("qcustomplot") or d.count("sqlite3"):
#                     continue
#                 path_list.append(d)
#                 #print("dir = ",d)
#                 f(d)
def f(path):
    global total;
    for filepath,dirnames,filenames in os.walk(path):
        for filename in filenames:
            if filename.count(".h") or filename.count(".cpp") or filename.count(".py") or filename.count(".pro") or filename.count(".log"):
                if not filename.count("sqlite3") and not filename.count("qcustomplot") and not filename.count("plotexamples"):
                    p = os.path.join(filepath,filename)
                    print(p)
                    count = len(open(p, 'r',encoding="utf-8").readlines())
                    total += count              

if __name__ == '__main__':
    f(path1)
    #f(path2)
  
    # print("dir's count = ",len(path_list))
    # print(path_list)
    # print("file's count = ",len(file_list))
    # print(file_list)
    print("total lines = ",total)

    # os.system("pause")
    time.sleep(1)