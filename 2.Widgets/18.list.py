from PyQt5.QtWidgets import QApplication, QListWidget, QMessageBox, QWidget

class MyListWidget(QListWidget):
    def clicked(self, item):
        QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())

def main():
    app = QApplication([])
    listWidget = MyListWidget()

    # Resize width and height
    listWidget.resize(300, 120)

    listWidget.addItem("Item 1")
    listWidget.addItem("Item 2")
    listWidget.addItem("Item 3")
    listWidget.addItem("Item 4")

    listWidget.setWindowTitle('PyQt5 QListWidget Demo')
    listWidget.itemClicked.connect(listWidget.clicked)

    listWidget.show()
    app.exec_()

if __name__ == '__main__':
    main()
