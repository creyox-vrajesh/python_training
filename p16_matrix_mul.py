arr1 = [[1,2],[1,2],[1,2]] #3*2
arr2 = [[1,2,3,4],[1,2,3,4]] #2*4

print(len(arr1))
print(len(arr1[0]))
print(len(arr2))
print(len(arr2[0]))

arr3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print(len(arr3[0]))

for i in range(len(arr1)):
  for j in range(len(arr2[0])):
    result = 0
    
    for k in range(len(arr1[0])):
        result = result + arr1[i][k] * arr2[k][j]

    arr3[i][j] = result

print(arr3)