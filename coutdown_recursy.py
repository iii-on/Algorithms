def coutdown(i):
    print(i)
    if i<= 1:
        return
    else:
        coutdown(i-1)
        
coutdown(10)