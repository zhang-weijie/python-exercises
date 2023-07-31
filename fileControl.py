def file_save(libai,dufu,count):
    file_name_libai='李白'+str(count)+'.txt'
    file_name_dufu='杜甫'+str(count)+'.txt'
    libai_file=open('D:\\'+file_name_libai,'w')
    dufu_file=open('D:\\'+file_name_dufu,'w')
    libai_file.writelines(libai)
    dufu_file.writelines(dufu)
    libai_file.close()
    dufu_file.close()
    libai=[]
    dufu=[]
    count+=1
def file_setup(trace):
    f=open(trace)
    libai=[]
    dufu=[]
    count=1
    for eachline in f:
        if eachline[:1]!='=':
            (role,linespoken)=eachline.split('：',1)
            if role=='李白':
                libai.append(linespoken)
            else:
                dufu.append(linespoken)
        else:
            file_save(libai,dufu,count)
    file_save(libai,dufu,count)        
    f.close()
trace=input('输入您要分割的文件的路径：')
file_setup(trace)
    
