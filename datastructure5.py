def getNoOfColumns(arr):
    """Passed in argument must be  a 2-d array"""

    #Assert that what we get is atleast a 2d array
    assert isinstance(arr,list)
    for i in range(len(arr)):
        assert isinstance(arr[i],list)
    
    #Assert that all rows have same no. of columns
    colCount = 0
    for i in range(len(arr)):
        if (colCount != 0):
            assert colCount == len(arr[i])
        else:
            colCount = len(arr[i])

    return colCount



matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

transpose=[]
rowCount = len(matrix)
colCount = getNoOfColumns(matrix)

print(f"No. of Rows={rowCount}")
print(f"No. of columns={colCount}")

for j in range(colCount):
    row = []
    transpose.append(row)
    for i in range(rowCount):
        row.append(matrix[i][j])
    #     print(matrix[i][j])
    # print("-" * 5)

# for row in matrix:
#     print(row)

print("*matrix=",*matrix)
print(f"matrix={matrix}")
print(f"transpose={transpose}")

