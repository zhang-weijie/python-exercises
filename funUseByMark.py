import time
from functools import wraps
def timeslong(func):

    def __timeslong():
        start = time.clock()
        print("It's time starting ! ",func.__name__)
        func()
        print("It's time ending ! ")
        end = time.clock()
        return "It's used : %s ." % (end - start)
    return __timeslong


@timeslong
def get_file_size():
    import os
    import os.path
    file_list=os.listdir()
    for each_file in file_list:
        file_size=os.path.getsize('C:\\安装应用\\Python 3.3.2\\练习'+os.sep+each_file)
        print(each_file+'文件的大小为%d个字节'%file_size)

print(get_file_size())


