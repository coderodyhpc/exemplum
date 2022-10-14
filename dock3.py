from PyQt5 import QtGui, QtWidgets

class TabBar(QtWidgets.QTabBar):
    def paintEvent(self, event):
        style = self.style()
        painter = QtGui.QPainter(self)
        option = QtWidgets.QStyleOptionTab()
        for index in range(self.count()):
            self.initStyleOption(option, index)
            bgcolor = QtGui.QColor(self.tabText(index))
            option.palette.setColor(QtGui.QPalette.Window, bgcolor)
            style.drawControl(QtWidgets.QStyle.CE_TabBarTab, option, painter)

class Window(QtWidgets.QTabWidget):
    def __init__(self):
        super().__init__()
        self.setTabBar(TabBar(self))
        for color in 'tomato orange yellow lightgreen skyblue plum'.split():
            self.addTab(QtWidgets.QWidget(self), color)

if __name__ == '__main__':

    app = QtWidgets.QApplication(['COLORIN'])
    window = Window()
    window.setGeometry(600, 100, 420, 200)
    window.show()
    app.exec()
    
    
