def Sorting(unsorted_nums):
        length=len(unsorted_nums)
        for i in range(length-1):
                if unsorted_nums[i]>unsorted_nums[i+1]:
                        temp=unsorted_nums.pop(i+1)
                        for k in range(i+1):
                                if unsorted_nums[k]>temp:
                                        unsorted_nums.insert(k,temp)
                                        break
        print(unsorted_nums)
                                
                

nums=input("请输入一串整数：")
nums=nums.split(",")
unsorted_nums=[]
for each in nums:
        unsorted_nums.append(int(each))
Sorting(unsorted_nums)     
        
        
