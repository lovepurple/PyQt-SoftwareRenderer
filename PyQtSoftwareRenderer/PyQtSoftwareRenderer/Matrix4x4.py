'''
    于Unity的Matrix4x4 一致
'''
from Vector import Vector3

class Matrix4x4(object):

    def __init__(self, matrixData=None):
        self._matrixData = [[0] * 4] * 4

        if(not(matrixData == None)):
            if(len(matrixData) != 4):
                return

            if(len(matrixData[0]) != 4):
                return

            for rowIndex in range(0,len(matrixData)):
                self._matrixData[rowIndex] = matrixData[rowIndex]


    def __add__(self,other):
        if(not isinstance(other,Matrix4x4)):
            raise TypeError("type error")

        list_add = lambda list1,list2:[x + y for x,y in zip(list1,list2)]

        finalMatrixList = []

        for x,y in zip(self._matrixData,other._matrixData):
            finalMatrixList.append(list_add(x,y))

        return Matrix4x4(finalResult)
       
    def __sub__(self,other):
        if(not isinstance(other,Matrix4x4)):
            raise TypeError("type error")

        list_sub = lambda list1,list2 :[x - y for x,y in zip(list1,list2)]
        
        finalresult = []

        for x,y in zip(self._matrixData,other._matrixData):
            finalresult.append(list_sub(x,y))

        return Matrix4x4(finalresult)

    def transpose(self):
        #matrixDataList = [[0] * 4 for i in range(4)]
        matrixDataList = [[0 for j in range(4) ] for i in range(4)]
        
        for rowIndex in range(0,len(self._matrixData)):
            for columnIndex in range(0,len(self._matrixData[rowIndex])):
                matrixElement = self._matrixData[rowIndex][columnIndex]
                matrixDataList[columnIndex][rowIndex] = matrixElement

        return Matrix4x4(matrixDataList)

    def __str__(self):
        strAfterFormat = str()
        formatStr = '{:2},{:2},{:2},{:2}\n'

        for row in self._matrixData:
          strAfterFormat += formatStr.format(row[0],row[1],row[2],row[3])

        return strAfterFormat[:len(strAfterFormat) - 1]





    def getRow(self,row):
        return
    #    if(row > 3):
    #        raise IndexError("index error")

    #    if(row == 0):
    #        return Vector3(self._m00,self._m01,self._m02,self._m03)
    #    elif(row == 1):
    #        return Vector3(self._m10,self._m11,self._m12,self._m13)
    #    elif(row == 2):
    #        return Vector3(self._m20,self._m21,self._m22,self._m23)
    #    elif(row == 3):
    #        return Vector3(self._m30,self._m31,self._m32,self._m33)
    #    else:



    def setRow(self,rowIndex,rowData):
        currentRowData = self.getRow(rowIndex)

        if(currentRowData != None):
            for i in range(0,len(rowData)):
                currentRowData[i] = rowData[i]
