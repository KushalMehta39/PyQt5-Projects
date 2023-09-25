import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def window():
    app = QApplication(sys.argv)
    w = QWidget()

    b = QPushButton(w)
    b.setText("Hello World!")
    b.move(90, 20)

    w.setGeometry(50, 50, 300, 200)
    w.setWindowTitle("PyQt")
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
