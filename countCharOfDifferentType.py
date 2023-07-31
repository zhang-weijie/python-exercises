def type_stream(*streams):


    for i in range(len(streams)):
        letters=0
        digits=0
        space=0
        others=0

        for each in streams[i]:
            if each.isalpha():
                letters+=1
            elif each.isdigit():
                digits+=1
            elif each==' ':
                space+=1
            else:
                others+=1                

        print('第%d串字符的英文字母有%d个，数字有%d个，空格有%d个，其他字符有%d个'%(i+1,letters,digits,space,others))






        
        


    
            
        
    
