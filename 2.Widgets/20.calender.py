import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout(self)
        
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked.connect(self.showDate)
        
        self.lbl = QLabel(self)
        layout.addWidget(cal)
        layout.addWidget(self.lbl)
        
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Calendar')
        self.show()
    
    def showDate(self, date):
        self.lbl.setText(date.toString(Qt.ISODate))

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
