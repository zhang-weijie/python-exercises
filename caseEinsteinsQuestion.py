s=1
n=0
while n<1:
    if s%2==1:
        if s%3==2:
            if s%5==4:
                if s%6==5:
                    if s%7==0:
                        print(s)
                        n=n+1
                    else:
                        s=s+1
                else:
                    s=s+1
            else:
                s=s+1
        else:
            s=s+1
    else:
        s=s+1


            
