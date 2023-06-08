from app import *
from PyQt5.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    win = Window(app)
    win.show()
    sys.exit(app.exec_())
main()