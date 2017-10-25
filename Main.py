import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

import biblio_fuzzy as bf

class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Recomendador de videojuegos')
        self.setGeometry(500, 100, 500, 150)
        self._initUI()
        self.show()
    
    def _initUI(self):
        duracion_lbl = QtWidgets.QLabel("Duracion.")
        estrateg_lbl = QtWidgets.QLabel("Estrategia.")
        accion_lbl = QtWidgets.QLabel("Accion.")
        dificult_lbl = QtWidgets.QLabel("Dificultad.")
        explorac_lbl = QtWidgets.QLabel("Exploracion.")
        sangre_lbl = QtWidgets.QLabel("Sangre")

        duracion_sld = QtWidgets.QSlider()
        duracion_sld.setMaximumHeight(50)
        estrateg_sld = QtWidgets.QSlider()
        estrateg_sld.setMaximumHeight(50)
        accion_sld = QtWidgets.QSlider()
        accion_sld.setMaximumHeight(50)
        dificult_sld = QtWidgets.QSlider()
        dificult_sld.setMaximumHeight(50)
        explorac_sld = QtWidgets.QSlider()
        explorac_sld.setMaximumHeight(50)
        sangre_sld = QtWidgets.QSlider()
        sangre_sld.setMaximumHeight(50)

        calc_rec_btn = QtWidgets.QPushButton("Generar.")

        grid = QtWidgets.QGridLayout(self)
        grid.addWidget(duracion_lbl, 0, 0)
        grid.addWidget(duracion_sld, 1, 0)
        grid.addWidget(estrateg_lbl, 0, 1)
        grid.addWidget(estrateg_sld, 1, 1)
        grid.addWidget(accion_lbl, 0, 2)
        grid.addWidget(accion_sld, 1, 2)
        grid.addWidget(dificult_lbl, 0, 3)
        grid.addWidget(dificult_sld, 1, 3)
        grid.addWidget(explorac_lbl, 0, 4)
        grid.addWidget(explorac_sld, 1, 4)
        grid.addWidget(sangre_lbl, 0, 5)
        grid.addWidget(sangre_sld, 1, 5)
        grid.addWidget(calc_rec_btn, 3, 6)

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())