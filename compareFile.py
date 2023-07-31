def compare_files(file_name1,file_name2):
    file1=open('D:\\'+file_name1+'.py')
    file2=open('D:\\'+file_name2+'.py')
    lines_list1=file1.readlines()
    lines_list2=file2.readlines()
    length1=min(len(lines_list1),len(lines_list2))
    for i in range(length1):

        length_lines1=len(lines_list1[i])
        length_lines2=len(lines_list2[i])
        length2=min(length_lines1,length_lines2)
        for m in range(length2):
            if lines_list1[i][m]!=lines_list2[i][m]:
                print('第%d行第%d个字符不同'%(i,m))
                
            
            
            
    
    

file_name1=input('请输入第一个文件名：')
file_name2=input('请输入第二个文件名：')
compare_files(file_name1,file_name2)
    



       
        
        
        
    


    
