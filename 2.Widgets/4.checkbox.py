import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CheckDemo(QWidget):
   def __init__(self, parent = None):
      super(CheckDemo, self).__init__(parent)
      
      layout = QHBoxLayout()
      self.b1 = QCheckBox("Tea")
      self.b1.setChecked(True)
      self.b1.stateChanged.connect(lambda: self.btnstate(self.b1))
      layout.addWidget(self.b1)
      
      self.b2 = QCheckBox("Coffee")
      self.b2.toggled.connect(lambda: self.btnstate(self.b2))
      layout.addWidget(self.b2)
      
      self.setLayout(layout)
      self.setWindowTitle("Menu")
      
      # Set a minimum window size
      self.setMinimumSize(300, 100)

   def btnstate(self, b):
      selected = []
      
      if self.b1.isChecked():
         selected.append("Tea")
         
      if self.b2.isChecked():
         selected.append("Coffee")
         
      if not selected:
         print("No, I am okay. I don't want Tea or Coffee.")
      else:
         print("I want " + " and ".join(selected))

def main():
   app = QApplication(sys.argv)
   ex = CheckDemo()
   ex.show()
   sys.exit(app.exec_())
   
if __name__ == '__main__':
   main()
