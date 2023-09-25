import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FileDialogDemo(QWidget):
   def __init__(self, parent=None):
      super(FileDialogDemo, self).__init__(parent)
		
      layout = QVBoxLayout()
      self.btn = QPushButton("Open Images")
      self.btn.clicked.connect(self.getfile)
		
      layout.addWidget(self.btn)
      self.label = QLabel("Kushal Mehta")
      self.label.setAlignment(Qt.AlignCenter)
		
      layout.addWidget(self.label)
      self.btn1 = QPushButton("Open Files")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)
		
      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.setLayout(layout)
      self.setWindowTitle("File Dialog demo")
		
   def getfile(self):
      options = QFileDialog.Options()
      options |= QFileDialog.ReadOnly
      fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',
         "Image files (*.jpg *.gif);;All Files (*)", options=options)
      if fname:
         pixmap = QPixmap(fname)
         self.label.setPixmap(pixmap)
		
   def getfiles(self):
      dlg = QFileDialog()
      dlg.setFileMode(QFileDialog.ExistingFiles)
      dlg.setNameFilter("Text files (*.txt)")
      filenames = []  # Use a regular Python list
		
      if dlg.exec_():
         filenames = dlg.selectedFiles()
         if filenames:
            with open(filenames[0], 'r') as f:
               data = f.read()
               self.contents.setText(data)
				
def main():
   app = QApplication(sys.argv)
   ex = FileDialogDemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
