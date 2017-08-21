import Vector

class Test_TestVector():
    def __init__(self):
        self.vector3Instance = Vector.Vector3(1,2,3)
        self.otherVector3Instance = Vector.Vector3(4,5,6)
        self.thridVector3Instance = Vector.Vector3(1,2,3)

    
    def testadd(self):
        result = self.vector3Instance + self.otherVector3Instance
        result.zero()
        return result

    def testNormalize(self):
        return self.otherVector3Instance.normalize()

    def testDiv(self):
        return self.vector3Instance / 3

    def testEqual(self):
        return self.otherVector3Instance == self.vector3Instance,self.thridVector3Instance == self.vector3Instance

    def testProperty(self):
        return self.vector3Instance.x

if __name__ == '__main__':
    list1 = [[1,2,3,4],[1,2,3,4]]
    list2 = [[1,2,3],[1,2,3]]

    vec_add = lambda x,y:tuple(zip(list1,list2))

    vec_add = lambda a,b : tuple([x + y for x,y in zip(a,b)])
    result = vec_add(list1,list2)
    print(result)