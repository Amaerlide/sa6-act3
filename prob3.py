def max(lst, lmbda):
    max = lst[0]

    for n in lst:
        if lmbda(n, max) > 0:
            max = n
    
    return max


lst = [5,10,20,15,1,100]

comp = lambda x, y: x if x > y else y

print(max(lst, comp))