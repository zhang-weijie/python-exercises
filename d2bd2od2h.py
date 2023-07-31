temp=input('请输入一个整数（输入Q结束程序）：')
if temp=='Q':
    print('程序结束')
else:
    num0=int(temp)
    num1='%x'% num0
    num2='%o'% num0
    num3=bin(num0)
    num1='0x'+str(num1)
    num2='0o'+str(num2)

    print('十进制->十六进制：',num0,'->',num1)
    print('十进制->八进制：',num0,'->',num2)
    print('十进制->二进制：',num0,'->',num3)


