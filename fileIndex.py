def file_index(dir_name):
    import os
    
    files_list=os.listdir(dir_name)
    f_ext_list=[]
    f_ext_set=set()

    for each_line in files_list:
        (f_name,f_ext)=os.path.splitext(each_line)
        f_ext_list.append(f_ext)
        f_ext_set.add(f_ext)
    for each_ext in f_ext_set:
        if each_ext=='':
            print('当前目录下共有【文件夹】%d个'%f_ext_list.count(each_ext))
        else:
            print('当前目录下共有【%s】文件%d'%(each_ext,f_ext_list.count(each_ext)))
        
dir_name=input('请输入要检索的目录：')
file_index(dir_name)
            
        
    
