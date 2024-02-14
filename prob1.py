from functools import reduce

num = 1379

num_st = str(num)

result = reduce(lambda x,y: int(x) + int(y),num_st)

print(result)