def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
    
a = sum(10)
print(a) 