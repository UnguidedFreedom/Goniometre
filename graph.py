from PySide import QtCore, QtGui
from random import randint
import sys

class Graph(QtGui.QWidget):
    def __init__(self):
        """
        Desc:   Initialize the Graph display widget
        Input:  self
        Output: None
        """
        QtGui.QWidget.__init__(self)
        self.setMouseTracking(True)

        self.angles = []
        angle = 180
        n = 50
        w = 500/n
        for i in range(n+1):
            angle += randint(-w,w)
            angle = min(max(angle, 0), 360)
            self.angles.append((w*i, angle))

    def cursor_position(self):
        """
        Desc:   Return the position on the board of the mouse cursor
        Input:  self
        Output: position (tuple(int))
        """
        pos = self.mapFromGlobal(QtGui.QCursor().pos())
        return (pos.y()-29)//52, (pos.x()-29)//52

    def paintEvent(self, *args, **kwargs):
        """
        Desc:   Redraw the entire board
        Input:  self, args, kwargs (default PySide arguments)
        Output: None
        """
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        maxTime = self.angles[-1][0]

        w = self.width()
        h = self.height()

        polygon = QtGui.QPolygonF()

        curx = self.mapFromGlobal(QtGui.QCursor().pos()).x()
        closestx = 2*w
        closesty = 2*h

        for i in range(len(self.angles)):
            time, pos = self.angles[i]
            x = time*w/maxTime
            y = h*(1-pos/360)
            if abs(x-curx) < abs(closestx-curx) :
                closestx = x
                closesty = y
            polygon.append(QtCore.QPointF(x,y))

        if self.underMouse():
            r = 7
            painter.setBrush(QtGui.QColor(0,127,255))
            painter.setPen(QtGui.QPen(QtGui.QColor(0,127,255), 2))
            painter.drawEllipse(closestx-r/2, closesty-r/2, r, r)
            painter.setBrush(QtGui.QColor(0,127,255, 63))
        else:
            painter.setPen(QtGui.QPen(QtGui.QColor(0,127,255), 1))
            painter.setBrush(QtGui.QColor(0,127,255, 50))

        painter.drawPolyline(polygon)

        painter.setPen(QtGui.QPen(QtGui.QColor(0,127,255, 0), 0))

        polygon.append(QtCore.QPointF(w,h))
        polygon.append(QtCore.QPointF(0,h))

        painter.drawPolygon(polygon)

        painter.end()

    def mousePressEvent(self, *args, **kwargs):
        """
        Desc:   Gestion of mouse click
        Input:  self, args, kwargs (default PySide arguments)
        Output: None
        """
        x, y = self.cursor_position()
        if 0 <= x <= 9 and 0 <= y <= 9 and self.display.word_input.text()!="":
            self.display.x_input.setValue(x)
            self.display.y_input.setValue(y)
            self.display.validate()

    def mouseMoveEvent(self, event):
        # print(event.x(), event.y())
        self.repaint()

    def leaveEvent(self, event):
        self.repaint()


class Goniometer(object):
    def __init__(self):
        """
        Desc:   Initialize the game GUI
        Input:  self
        Output: None
        """
        self.app = QtGui.QApplication(sys.argv)
        self.setup()
        self.window.show()
        self.app.exec_()

    def setup(self):
        """
        Desc:   Setup the window
        Input:  self
        Output: None
        """
        self.window = QtGui.QMainWindow()
        self.window.setWindowTitle("Goniometer")
        self.window.resize(600,300)
        self.graph = Graph()
        self.window.setCentralWidget(self.graph)

gonio = Goniometer()