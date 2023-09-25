import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FontDialogDemo(QWidget):
   def __init__(self, parent=None):
      super(FontDialogDemo, self).__init__(parent)
      self.setMinimumSize(300, 200)
		
      layout = QVBoxLayout()
      self.btn = QPushButton("Choose Font-Style")
      self.btn.clicked.connect(self.getfont)
		
      layout.addWidget(self.btn)
      self.le = QLabel("Kushal Mehta")
      self.le.setAlignment(Qt.AlignCenter)
		
      layout.addWidget(self.le)
      self.setLayout(layout)
      self.setWindowTitle("Change Font Style")
		
   def getfont(self):
      font, ok = QFontDialog.getFont()
		
      if ok:
         self.le.setFont(font)
			
def main():
   app = QApplication(sys.argv)
   ex = FontDialogDemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
