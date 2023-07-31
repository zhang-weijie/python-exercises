list3=[]
list4=[]
list1=['1.Just do it','2.一切皆有可能','3.让编程改变世界','4.Nothing is impossible']
list2=['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
list2.sort()
for a in list1:
    for b in list2:
        if list1.index(a)==list2.index(b):
            list3.append([a,b])
print(list3)



    
        
