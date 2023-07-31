def bin1(x):
    list1=[]
    result=''
    while True:
        a=x//2
        b=x%2
        list1.append(b)
        if a==0:
            break
        x=a
    list1.reverse()
    for each in list1:
        result+=str(each)

    return result

x=int(input('请输入一个正整数：'))
result=bin1(x)
print(result)
    
        
    
        
