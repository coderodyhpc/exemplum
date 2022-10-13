import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QSpinBox, QApplication

class spindemo(QWidget):
   def __init__(self, parent = None):
      super(spindemo, self).__init__(parent)

      layout = QVBoxLayout()
      self.l1 = QLabel("Current value:")
      self.l1.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.l1)
      self.sp = QSpinBox()
      ini_val = 35                     # To set initial value
      self.sp.setRange(15,300)  # To set the range
      self.sp.setValue = ini_val

      layout.addWidget(self.sp)
      self.sp.valueChanged.connect(self.valuechange)
      self.setLayout(layout)
      self.setWindowTitle("SpinBox demo")

   def valuechange(self):
      self.l1.setText("current value:"+str(self.sp.value()))

def main():
   app = QApplication(sys.argv)
   ex = spindemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()

