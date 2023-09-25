import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class InputDialogDemo(QWidget):
   def __init__(self, parent=None):
      super(InputDialogDemo, self).__init__(parent)
      self.setMinimumSize(300, 200)
      
      layout = QFormLayout()
      self.btn = QPushButton("Languange")
      self.btn.clicked.connect(self.getItem)
      
      self.le = QLineEdit()
      layout.addRow(self.btn, self.le)
      
      self.btn1 = QPushButton("Name")
      self.btn1.clicked.connect(self.getText)
      
      self.le1 = QLineEdit()
      layout.addRow(self.btn1, self.le1)
      
      self.btn2 = QPushButton("Experience")
      self.btn2.clicked.connect(self.getInt)
      
      self.le2 = QLineEdit()
      layout.addRow(self.btn2, self.le2)
      
      self.setLayout(layout)
      self.setWindowTitle("Input Dialog Demo")
      
   def getItem(self):
      items = ("C", "C++", "Java", "Python")
      
      item, ok = QInputDialog.getItem(
         self, "Select Input Dialog", "List of languages", items, 0, False
      )
      
      if ok and item:
         self.le.setText(item)
      
   def getText(self):
      text, ok = QInputDialog.getText(self, 'Personal Data', 'Enter your name:')
      
      if ok:
         self.le1.setText(text)
      
   def getInt(self):
      num, ok = QInputDialog.getInt(self, "Experience of", "Years:")
      
      if ok:
         self.le2.setText(str(num))

def main():
   app = QApplication(sys.argv)
   ex = InputDialogDemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
