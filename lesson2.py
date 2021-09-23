array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
result = []
for i,x in enumerate(array):
    if x%3==0:
        result.append((x,i))

print(result)