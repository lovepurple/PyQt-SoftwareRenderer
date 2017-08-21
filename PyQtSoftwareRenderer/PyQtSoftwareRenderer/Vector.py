#from __future__ import division
import math
'''
    与Unity 一致 使用列向量 3 * 1 
'''
 

class Vector3():
    
    def __init__(self, x,y,z):
        self._x = x
        self._y = y
        self._z = z

    def __add__(self,other):
        return Vector3(self._x + other.x,self._y + other.y,self._z + other.z)

    def __sub__(self,other):
        return Vector3(self._x - other.x,self._y - other.y,self._z - other.z)

    def __mul__(self,scalar):
        return Vector3(self._x * scalar,self._y * scalar,self._z * scalar)

    def __eq__(self, other):
       return (self._x == other.x) and (self._y == other.y) and (self._z == other.z)

    def __ne__(self, other):
        return not (self == other)


    def __truediv__(self,scalar):
        if(scalar == 0):
            return None
        else:
            scalar = 1 / scalar
            return  self * scalar
    
    def squareDistance(vectorA,vectorB=None):
        if(vectorB == None):
            vectorB = Vector3.Zero()

        squareX = math.pow((vectorA.x - vectorB.x),2)
        squareY = math.pow((vectorA.y - vectorB.y),2)
        squareZ = math.pow((vectorA.z - vectorB.z),2)

        return squareX + squareY + squareZ

    def distance(vectorA,vectorB=None):
        if(vectorB == None):
            vectorB = Vector3.Zero()

        squareDistanceValue = Vector3.squareDistance(vectorA,vectorB)
        
        return math.sqrt(squareDistanceValue)

    def normalize(vector):
        vectorDistance = distance(vector)
        
        return vector / vectorDistance

    def dot(vectorLeft,vectorRight):
        return vectorLeft.x * vectorRight.x + vectorLeft.y * vectorRight.y + vectorLeft.z * vectorRight.z

    def cross(vectorLeft,vectorRight):
        x = vectorLeft.y * vectorRight.z - vectorLeft.z * vectorRight.y
        y = vectorLeft.z * vectorRight.x - vectorLeft.x * vectorRight.z
        z = vectorLeft.x * vectorRight.y - vectorLeft.y * vectorRight.x
    
        return Vector3(x,y,z)

    def __str__(self):
        return 'x:{:.4},y:{:.4},z:{:.4}'.format(self._x,self._y,self._z)

    def Zero():
        return Vector3(0,0,0)

    # Property in python

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

