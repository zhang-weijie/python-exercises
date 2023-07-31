def replace_file(file_name,word1,word2):
    file=open('D:\\'+file_name+'.txt')
    new_lines=[]
    for each_line in file:
        if word1 in each_line:
            new_line=each_line.replace(word1,word2)
            new_lines.append(new_line)
        else:
            new_lines.append(each_line)

    file.close()
    file=open('D:\\'+file_name+'.txt','w')
    file.writelines(new_lines)
    file.close()

file_name=input('请输入文件名：')
word1=input('请输入原有词汇：')
word2=input('请输入替换词汇：')
replace_file(file_name,word1,word2)
            
            
            
        

    
