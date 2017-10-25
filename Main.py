import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

import biblio_fuzzy as bf

class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Recomendador de videojuegos')
        self.setGeometry(500, 100, 300, 400)
        self._initUI()
        self.show()
    
    def _initUI(self):
        duracion_lbl = QtWidgets.QLabel("Duracion.")
        estrateg_lbl = QtWidgets.QLabel("Estrategia.")
        accion_lbl = QtWidgets.QLabel("Accion.")
        dificult_lbl = QtWidgets.QLabel("Dificultad.")
        explorac_lbl = QtWidgets.QLabel("Exploracion.")
        sangre_lbl = QtWidgets.QLabel("Sangre")

        duracion_sld = QtWidgets.QSlider(Qt.Horizontal)
        estrateg_sld = QtWidgets.QSlider(Qt.Horizontal)
        accion_sld = QtWidgets.QSlider(Qt.Horizontal)
        dificult_sld = QtWidgets.QSlider(Qt.Horizontal)
        explorac_sld = QtWidgets.QSlider(Qt.Horizontal)
        sangre_sld = QtWidgets.QSlider(Qt.Horizontal)

        calc_rec_btn = QtWidgets.QPushButton("Generar.")

        grid = QtWidgets.QGridLayout(self)
        grid.addWidget(duracion_lbl, 0, 0)
        grid.addWidget(duracion_sld, 1, 0)
        grid.addWidget(estrateg_lbl, 2, 0)
        grid.addWidget(estrateg_sld, 3, 0)
        grid.addWidget(accion_lbl, 4, 0)
        grid.addWidget(accion_sld, 5, 0)
        grid.addWidget(dificult_lbl, 6, 0)
        grid.addWidget(dificult_sld, 7, 0)
        grid.addWidget(explorac_lbl, 8, 0)
        grid.addWidget(explorac_sld, 9, 0)
        grid.addWidget(sangre_lbl, 10, 0)
        grid.addWidget(sangre_sld, 11, 0)
        grid.addWidget(calc_rec_btn, 12, 1)

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())