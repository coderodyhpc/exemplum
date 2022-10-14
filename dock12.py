import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QAction, QTabWidget, QVBoxLayout, QTabBar, QStyleOptionTab, QStyle 
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPainter, QColor, QPalette

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Tabs tailoring'
        self.setWindowTitle(self.title)

        self.table_widget = TailoredWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()
        
class TailoredTab(QTabBar):
    def paintEvent(self, event):
        style = self.style()
        painter = QPainter(self)
        option = QStyleOptionTab()
        for index in range(self.count()):
            self.initStyleOption(option, index)
            bgcolor = QColor(self.tabText(index))
            option.palette.setColor(QPalette.Window, bgcolor)
            style.drawControl(QStyle.CE_TabBarTab, option, painter)

class TailoredWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
#        self.tabs.setStyleSheet('''QTabBar::tab {font-size: 20pt; color: #00004F; height: 40px; width: 140px;}''')
        self.setTabBar(TailoredBar(self))
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        # Add tabs
        self.tabs.addTab(self.tab1,"TAB 1")
        self.tabs.addTab(self.tab2,"TAB 2")
        self.tabs.addTab(self.tab3,"TAB 3")

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
