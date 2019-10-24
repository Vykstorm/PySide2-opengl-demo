
import sys
from PySide2.QtWidgets import QOpenGLWidget, QDialog, QApplication, QVBoxLayout, QLineEdit
from PySide2.QtOpenGLFunctions import *
from PySide2.QtGui import QPainter
from math import pi, sin, cos


try:
    from OpenGL import GL
except ImportError:
    app = QtWidgets.QApplication(sys.argv)
    messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "OpenGL hellogl",
                                       "PyOpenGL must be installed to run this example.",
                                       QtWidgets.QMessageBox.Close)
    messageBox.setDetailedText("Run:\npip install PyOpenGL PyOpenGL_accelerate")
    messageBox.exec_()
    sys.exit(1)




class Renderer(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.startTimer(10)
        self.angular_speed = 0.25*360
        self.angle = 0


    def initializeGL(self):
        print("Initializing OpenGL")


    def resizeGL(self, width, height):
        print(f"Resizing window: {width}x{height}")

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()

        GL.glRotate(self.angle, 0, 0, 1)


        GL.glBegin(GL.GL_QUADS)
        GL.glColor(0.1, 0.5, 0)
        GL.glVertex(-0.5, -0.5)
        GL.glVertex(-0.5, 0.5)
        GL.glVertex(0.5, 0.5)
        GL.glVertex(0.5, -0.5)
        GL.glEnd()


    def timerEvent(self, event):
        self.angle += self.angular_speed / 100
        self.update()




class Main(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.renderer = Renderer()
        self.edit = QLineEdit('Hello world')
        layout.addWidget(self.renderer)
        layout.addWidget(self.edit)
        self.setLayout(layout)
        self.resize(640, 480)




if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    main = Main()
    main.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
