import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SliderDemo(QWidget):
   def __init__(self, parent = None):
      super(SliderDemo, self).__init__(parent)
      self.setMinimumSize(300, 100)

      layout = QVBoxLayout()
      self.l1 = QLabel("Kushal")
      self.l1.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.l1)
      
      self.sl = QSlider(Qt.Horizontal)
      self.sl.setMinimum(10)
      self.sl.setMaximum(30)
      self.sl.setValue(20)
      self.sl.setTickPosition(QSlider.TicksBelow)
      self.sl.setTickInterval(5)
      
      layout.addWidget(self.sl)
      self.sl.valueChanged.connect(self.valuechange)
      self.setLayout(layout)
      self.setWindowTitle("Change Font-Size")  # Set the correct window title

   def valuechange(self):
      size = self.sl.value()
      self.l1.setFont(QFont("Arial", size))

def main():
   app = QApplication(sys.argv)
   ex = SliderDemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
