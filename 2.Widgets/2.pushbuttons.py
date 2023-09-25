import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton

class ButtonDemo(QDialog):
    def __init__(self, parent=None):
        super(ButtonDemo, self).__init__(parent)
        self.setWindowTitle("Button Demo")
        self.setMinimumSize(400, 200)  # Set a minimum window size
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Button 1: Checkable Button
        self.b1 = QPushButton("Button 1")
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b1.clicked.connect(self.btnClicked)
        layout.addWidget(self.b1)

        # Button 2: Button with Icon
        self.b2 = QPushButton()
        self.b2.setIcon(QIcon(QPixmap("2.Widgets/Images/python.gif")))
        self.b2.clicked.connect(self.btnClicked)
        layout.addWidget(self.b2)

        # Button 3: Disabled Button
        self.b3 = QPushButton("Disabled")
        self.b3.setEnabled(False)
        layout.addWidget(self.b3)

        # Button 4: Default Button
        self.b4 = QPushButton("Default")
        self.b4.setDefault(True)
        self.b4.clicked.connect(self.btnClicked)
        layout.addWidget(self.b4)

        self.setLayout(layout)

    def btnClicked(self):
        sender = self.sender()
        if sender == self.b1:
            state = "pressed" if self.b1.isChecked() else "released"
        elif sender == self.b2:
            state = "clicked"
        elif sender == self.b4:
            state = "clicked (default)"
        else:
            state = "N/A"
        print(f"{sender.text()} was {state}")

def main():
    app = QApplication(sys.argv)
    demo = ButtonDemo()
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
