def fibbonachy(n):
    if n in (1,2):
        return 1
    return fibbonachy(n-1)+fibbonachy(n-2)
        
print(fibbonachy(6))