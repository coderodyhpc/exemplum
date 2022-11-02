import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Tabs tailoring'
        self.setWindowTitle(self.title)

        self.table_widget = TailoredWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

class TailoredWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet('''QTabBar::tab {font-size: 30pt; height: 40px; width: 140px;}''')
#        self.tabs.tabBar.setTabTextColor(1, color: #AA004F)
        self.tab1 = QWidget()
#        self.tab1.setStyleSheet('''QTabBar::tab {font-size: 15pt; color: #55004F; height: 40px; width: 140px;}''')
        self.tab1.tabBar.setTabTextColor('#55004F')
        self.tab2 = QWidget()
#        self.tab2.setStyleSheet('''QTabBar::tab {font-size: 20pt; color: #AA004F; height: 40px; width: 140px;}''')
        self.tab2.tabBar.setTabTextColor('#AA004F')
        self.tab3 = QWidget()
#        self.tab3.setStyleSheet('''QTabBar::tab {font-size: 25pt; color: #FF004F; height: 40px; width: 140px;}''')
        self.tab3.tabBar.setTabTextColor('#FF004F')

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
