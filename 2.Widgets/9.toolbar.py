import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ToolDemo(QMainWindow):
   def __init__(self, parent=None):
      super(ToolDemo, self).__init__(parent)
      self.setMinimumSize(300, 200)
      
      layout = QVBoxLayout()
      toolbar = self.addToolBar("File")
      
      new_action = QAction(QIcon("2.Widgets/Images/new.png"), "New", self)
      toolbar.addAction(new_action)
      
      open_action = QAction(QIcon("2.Widgets/Images/open.png"), "Open", self)
      toolbar.addAction(open_action)
      
      save_action = QAction(QIcon("2.Widgets/Images/save.png"), "Save", self)
      toolbar.addAction(save_action)
      
      toolbar.actionTriggered[QAction].connect(self.toolBtnPressed)
      
      self.setWindowTitle("Toolbar Demo")

   def toolBtnPressed(self, action):
      print("Pressed tool button:", action.text())

def main():
   app = QApplication(sys.argv)
   ex = ToolDemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
