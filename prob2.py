lst = ['Hi', 'Hey', 'Hello','something', 'Bake', 'four']

result = sorted(lst, key= lambda x: (len(x), x))

print(result)