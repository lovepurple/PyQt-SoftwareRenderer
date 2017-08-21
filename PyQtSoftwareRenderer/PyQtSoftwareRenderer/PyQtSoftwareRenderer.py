import sys
from PyQt5 import QtCore,QtGui,QtOpenGL
import Vector


class MyQWindow(QtGui.QWindow):
    def __init__(self):
        QtGui.QWindow.__init__(self)
        self.setTitle("MyQWindow")
        self.setWidth(800)
        self.setHeight(800)
        
class MyOpenGLWindow(QtGui.QOpenGLWindow):
    def __init__(self, **kwargs):
        QtGui.QOpenGLWindow.__init__(self)
        self.setTitle("MyQOpenGLWindow")
        self.setWidth(800)
        self.setHeight(800)

app = QtGui.QGuiApplication(sys.argv)
myWindow = MyOpenGLWindow()
myWindow.show()


app.exec_();

