import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SpinDemo(QWidget):
    def __init__(self, parent=None):
        super(SpinDemo, self).__init__(parent)
        self.setMinimumSize(300, 100)

        layout = QVBoxLayout()
        self.l1 = QLabel("Current value:")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)
        self.sp = QSpinBox()

        layout.addWidget(self.sp)
        self.sp.valueChanged.connect(self.valuechange)
        self.setLayout(layout)
        self.setWindowTitle("SpinBox")

    def valuechange(self):
        self.l1.setText("Current value: " + str(self.sp.value()))

def main():
    app = QApplication(sys.argv)
    ex = SpinDemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
