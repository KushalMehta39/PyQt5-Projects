import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ComboDemo(QWidget):
   def __init__(self, parent=None):
      super(ComboDemo, self).__init__(parent)
      self.setMinimumSize(300, 100)
      
      layout = QHBoxLayout()
      self.cb = QComboBox()
      self.cb.addItem("C")
      self.cb.addItem("C++")
      self.cb.addItems(["Java", "C#", "Python"])
      self.cb.currentIndexChanged.connect(self.selectionchange)
      
      layout.addWidget(self.cb)
      self.setLayout(layout)
      self.setWindowTitle("Select Your Languange")

   def selectionchange(self, i):
      print("Items in the list are:")
      
      for count in range(self.cb.count()):
         print(self.cb.itemText(count))
      print("Current index", i, "selection changed", self.cb.currentText())

def main():
   app = QApplication(sys.argv)
   ex = ComboDemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
