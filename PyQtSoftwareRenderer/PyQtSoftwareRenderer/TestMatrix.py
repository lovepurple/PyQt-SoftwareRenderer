import Matrix4x4


matrix = Matrix4x4.Matrix4x4([[1,2,3,4],
    [5,6,7,8],
    [1,2,3,4],
    [5,6,7,8]])

matrix2 = Matrix4x4.Matrix4x4([[1,2,3,4],
    [5,6,7,8],
    [1,2,3,4],
    [5,6,7,8]])


#按索引遍历
#for row in range(0,len(matrix._matrixData)):
#    for i in range(0,len(matrix._matrixData[row])):
#        matrix._matrixData[row][i] = i * 10

##按内容直接遍历
#for i in matrix._matrixData:
#    print(i)
#matrix_add = lambda matrixLeft,matrixRight:tuple([x + y for x,y in
#zip(matrixLeft._matrixData,matrixRight._matrixData)])
#result = matrix_add(matrix,matrix2)

#result2 = []
#mergere = None
#for item in result:
#    lista = item[:4]
#    listb = item[4:]
    
#    parallel_mergeList = lambda list1,list2:[x + y for x,y in
#    zip(list1,list2)]
#    mergere = parallel_mergeList(lista,listb)
#    result2.append(mergere)

#print(result2)

result = matrix - matrix2
print(matrix.transpose() - matrix2)
#matrix_add = lambda matrixLeft,matrixRight:[x + y for x,y in
#zip(matrixLeft._matrixData,matrixRight._matrixData)]
#result = matrix_add(matrix,matrix2)
#list1 = [[1,2,3],[4,5,6]]
#list2 = [[3,2,1],[6,5,4]]

##listMerge = zip(list1,list2)
##for x,y in listMerge:
##    list_add = lambda list1,list2 :[a + b for a,b in zip(list1,list2)]
##    result = list_add(x,y)
##    print(result)


##list_add = lambda list1,list2:[x + y for x,y in zip(list1,list2)]
##print(list_add(list1,list2))
#mergeList = zip(list1,list2)

#list_sub = lambda list1,list2:[x - y for x,y in zip(list1,list2)]
#for x,y in mergeList:
#    print([list_sub(x,y)])