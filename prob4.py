lst1 = [1,3,5,7,9,10,12]
lst2 = [1,2,4,6,8,10,12]

inter = list(filter(lambda x: x in lst1, lst2))

print(inter)