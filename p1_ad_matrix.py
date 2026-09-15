arr1 = [[1,2,3],[1,2,3],[1,2,3]]
arr2 = [[1,2,3],[1,2,3],[1,2,3]]
arr3 = [[0,0,0],[0,0,0],[0,0,0]]


for i in range(len(arr1)):
    for j in range(len(arr2)):
        arr3[i][j] = arr1[i][j] + arr2[i][j]


print(arr3)

