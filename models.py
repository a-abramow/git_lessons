from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowtitle("Первая программа на PyQT")
window.resize(300, 70)
label = QtWidgets.QLabel("<center>Привет, мир!</center>")
