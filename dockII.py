import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Tabs tailoring'
#        self.left = 0
#        self.top = 0
#        self.width = 300
#        self.height = 200
        self.setWindowTitle(self.title)
#        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.table_widget = TailoredWidget(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()
    
class TailoredWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet('''QTabBar::tab {font-size: 10pt; color: #00004F; height: 40px; width: 140px;}''')
        self.tab1 = QWidget()
#        self.tabs1.setStyleSheet('''QTabBar::tab {font-size: 10pt; color: #55004F; height: 40px; width: 140px;}''')
        self.tab2 = QWidget()
#        self.tabs2.setStyleSheet('''QTabBar::tab {font-size: 10pt; color: #AA004F; height: 40px; width: 140px;}''')
        self.tab3 = QWidget()
#        self.tabs3.setStyleSheet('''QTabBar::tab {font-size: 10pt; color: #FF004F; height: 40px; width: 140px;}''')
#        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"TAB 1")
        self.tabs.addTab(self.tab2,"TAB 2")
        self.tabs.addTab(self.tab3,"TAB 3")
        
        # Tab #1
        self.tab1.layout = QVBoxLayout(self)
        self.Button1 = QLabel("1-BAT")
        self.tab1.layout.addWidget(self.Button1)
        self.tab1.setLayout(self.tab1.layout)
        
        # Tab #2
        self.tab2.layout = QVBoxLayout(self)
        self.Button2 = QLabel("2-BAT")
        self.tab2.layout.addWidget(self.Button2)
        self.tab2.setLayout(self.tab2.layout)
        
        # Tab #3
        self.tab3.layout = QVBoxLayout(self)
        self.Button3 = QLabel1("3-BAT")
        self.tab3.layout.addWidget(self.Button3)
        self.tab3.setLayout(self.tab3.layout)
        
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
