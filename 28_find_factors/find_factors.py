def find_factors(n):
    newLst = []
    i = 1
    while(i < n+1):
        if n % i == 0:
            newLst.append(i)
        return newLst

print(find_factors(11))