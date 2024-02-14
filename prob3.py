def max(lst, lmbda):
    max_num = lst[0]

    for n in lst:
        max_num = lmbda(max_num,n)
    
    return max_num


lst = [5,100,20,15,1,2]

comp = lambda x, y: x if x > y else y

print(max(lst, comp))