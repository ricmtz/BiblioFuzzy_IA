import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

import sistema_fuzzy_juegos as sfj

class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()        
        self.__duracion = 0
        self.__estrategia = 0
        self.__accion = 0
        self.__dificultad = 0
        self.__exploracion = 0
        self.__violencia = 0
        self.setWindowTitle('Recomendador de videojuegos')
        self.setGeometry(500, 100, 400, 150)
        self._initUI()
        self.show()
    
    def _initUI(self):
        font_txt = QtGui.QFont()
        font_txt.setFamily('Arial')
        font_txt.setPointSize(10)        

        titulo_lbl = QtWidgets.QLabel("Recomendador de videojuegos.")
        titulo_lbl.setAlignment(Qt.AlignCenter)
        titulo_lbl.setFont(QtGui.QFont('Arial', 15))

        duracion_gbox = QtWidgets.QGroupBox('Duracion.')
        duracion_gbox.setFont(font_txt)
        estrateg_gbox = QtWidgets.QGroupBox('Estrategia')
        estrateg_gbox.setFont(font_txt)
        accion_gbox = QtWidgets.QGroupBox('Accion')
        accion_gbox.setFont(font_txt)
        dificult_gbox = QtWidgets.QGroupBox('Dificultad')
        dificult_gbox.setFont(font_txt)
        explorac_gbox = QtWidgets.QGroupBox('Exploracion')
        explorac_gbox.setFont(font_txt)
        violenci_gbox = QtWidgets.QGroupBox('Violencia')
        violenci_gbox.setFont(font_txt)

        duracion_vbox = QtWidgets.QHBoxLayout()
        estrateg_vbox = QtWidgets.QHBoxLayout()
        accion_vbox = QtWidgets.QHBoxLayout()
        dificult_vbox = QtWidgets.QHBoxLayout()
        explorac_vbox = QtWidgets.QHBoxLayout()
        violenci_vbox = QtWidgets.QHBoxLayout()

        duracion_sld = QtWidgets.QSlider()
        duracion_sld.setMinimumHeight(60)
        duracion_sld.valueChanged.connect(self.val_duracion)
        estrateg_sld = QtWidgets.QSlider()
        estrateg_sld.setMinimumHeight(60)
        estrateg_sld.valueChanged.connect(self.val_estrategia)
        accion_sld = QtWidgets.QSlider()
        accion_sld.setMinimumHeight(60)
        accion_sld.valueChanged.connect(self.val_accion)
        dificult_sld = QtWidgets.QSlider()
        dificult_sld.setMinimumHeight(60)
        dificult_sld.valueChanged.connect(self.val_dificultad)
        explorac_sld = QtWidgets.QSlider()
        explorac_sld.setMinimumHeight(60)
        explorac_sld.valueChanged.connect(self.val_exploracion)
        violenci_sld = QtWidgets.QSlider()
        violenci_sld.setMinimumHeight(60)
        violenci_sld.valueChanged.connect(self.val_violencia)

        calc_rec_btn = QtWidgets.QPushButton("Generar")
        calc_rec_btn.clicked.connect(self.generar_recomendacion)

        duracion_vbox.addWidget(duracion_sld)
        duracion_gbox.setLayout(duracion_vbox)     
        estrateg_vbox.addWidget(estrateg_sld)
        estrateg_gbox.setLayout(estrateg_vbox)
        accion_vbox.addWidget(accion_sld)
        accion_gbox.setLayout(accion_vbox)
        dificult_vbox.addWidget(dificult_sld)
        dificult_gbox.setLayout(dificult_vbox)
        explorac_vbox.addWidget(explorac_sld)
        explorac_gbox.setLayout(explorac_vbox)
        violenci_vbox.addWidget(violenci_sld)
        violenci_gbox.setLayout(violenci_vbox)

        grid = QtWidgets.QGridLayout(self)
        grid.addWidget(titulo_lbl, 0, 0, 1, 6)
        grid.addWidget(duracion_gbox, 1, 0)
        grid.addWidget(estrateg_gbox, 1, 1)
        grid.addWidget(accion_gbox, 1, 2)
        grid.addWidget(dificult_gbox, 1, 3)
        grid.addWidget(explorac_gbox, 1, 4)
        grid.addWidget(violenci_gbox, 1, 5)
        grid.addWidget(calc_rec_btn, 2, 5)
    
    def val_duracion(self, valor_d):
        self.__duracion = valor_d

    def val_estrategia(self, valor_e):
        self.__estrategia = valor_e
    
    def val_accion(self, valor_a):
        self.__accion = valor_a

    def val_dificultad(self, valor_d):
        self.__dificultad = valor_d
    
    def val_exploracion(self, valor_e):
        self.__exploracion = valor_e
    
    def val_violencia(self, valor_v):
        self.__violencia = valor_v
    
    def generar_recomendacion(self):
        __fuzzy = sfj.SistemaFuzzyJuegos()
        duracion_df = __fuzzy.fuzzificador_duracion(self.__duracion)
        estrategia_df = __fuzzy.fuzzificador_estrategia(self.__estrategia)
        accion_df = __fuzzy.fuzzificador_accion(self.__accion)
        dificultad_df = __fuzzy.fuzzificador_dificultad(self.__dificultad)
        exploracion_df = __fuzzy.fuzzificador_exploracion(self.__exploracion)
        sangre_df = __fuzzy.fuzzificador_sangre(self.__violencia)
        genero = __fuzzy.inferir_atributos_difusos_cualitativos(duracion_df, estrategia_df,
                                                                     accion_df, dificultad_df, 
                                                                     exploracion_df, sangre_df)
        if genero == "RPG":
            msg_rpg = ("El genero de juegos que te recomendamos es RPG.\n" +
                    "Te recomendamos:\n" +  "\t-Final Fantasy\n"+ "\t-The Legend of Zelda\n" +
                    "\t-Skyrim\n" + "\t-Fire Emblem" )
            mb_rpg = QtWidgets.QMessageBox.information(self, "Recomendacion", msg_rpg, QtWidgets.QMessageBox.Ok)            
        elif genero == "Plataformas":
            msg_plataform = ("El genero de juegos que te recomendamos es Plataformas.\n" +
                    "Te recomendamos:\n" +  "\t-Super Mario Bros\n"+ "\t-Megaman\n" +
                    "\t-Metroid\n" + "\t-Castelvania" )
            QtWidgets.QMessageBox.information(self, "Recomendacion", msg_plataform, QtWidgets.QMessageBox.Ok)
        elif genero == "Peleas":
            msg_peleas = ("El genero de juegos que te recomendamos es Peleas.\n" +
                    "Te recomendamos:\n" +  "\t-Street Fighter\n"+ "\t-God of War\n" +
                    "\t-Castle Crasher\n" + "\t-Devil May Cry" )
            QtWidgets.QMessageBox.information(self, "Recomendacion", msg_peleas, QtWidgets.QMessageBox.Ok)
        elif genero == "Disparos":
            msg_disparos = ("El genero de juegos que te recomendamos es Disparos.\n" +
                    "Te recomendamos:\n" +  "\t-Overwatch\n"+ "\t-Battlefield 1\n" +
                    "\t-Enter the Gungeon\n" + "\t-Gears of war" )
            QtWidgets.QMessageBox.information(self, "Recomendacion", msg_disparos, QtWidgets.QMessageBox.Ok)

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Main()    
    sys.exit(app.exec_())