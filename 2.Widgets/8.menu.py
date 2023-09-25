import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MenuDemo(QMainWindow):
   def __init__(self, parent=None):
      super(MenuDemo, self).__init__(parent)
      self.setMinimumSize(300, 400)
      
      layout = QHBoxLayout()
      bar = self.menuBar()
      file = bar.addMenu("File")
      file.addAction("New")
      
      save = QAction("Save", self)
      save.setShortcut("Ctrl+S")
      file.addAction(save)
      
      edit = QMenu("Edit", self)  # Create a submenu
      file.addMenu(edit)  # Add the submenu to the "File" menu
      edit.addAction("Copy")
      edit.addAction("Paste")
      
      quit = QAction("Quit", self)
      file.addAction(quit)
      file.triggered[QAction].connect(self.processTrigger)
      
      self.setWindowTitle("Word or Whatt!!!")

   def processTrigger(self, q):
      print(q.text() + " is triggered")

def main():
   app = QApplication(sys.argv)
   ex = MenuDemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
