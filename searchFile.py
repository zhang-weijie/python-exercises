import os
def search_file(start_dir,target_word):
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):
        if os.path.splitext(each_file)[1]=='.txt':
            target=os.getcwd()+os.sep+each_file
            target_file=open(target)
            lines_list=target_file.readlines()
            target_file.close()

            for each_line in lines_list:
                if target_word in each_line:
                    linenum=lines_list.index(each_line)+1
                    bytenum=each_line.find(target_word)
                    bytenum_list=[]
                    while bytenum!=-1:
                        bytenum_list.append(bytenum)
                        bytenum=each_line.find(target_word,bytenum+1)
                    print('您要查找的关键词出现在%s文件中的第%d行第%s位置'%(target,linenum,bytenum_list))        
                
        if os.path.isdir(each_file):
            search_file(each_file,target_word)
            os.chdir(os.pardir)

start_dir=input('请输入查找路径：')
target_word=input('请输入关键词：')
search_file(start_dir,target_word)


        
