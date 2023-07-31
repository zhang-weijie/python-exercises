def gcd(x,y):
    large=max(x,y)
    tiny=min(x,y)
    temp=large%tiny
    if temp==0:
        return tiny
    else:
        gcd(tiny,temp)

    
        
    






