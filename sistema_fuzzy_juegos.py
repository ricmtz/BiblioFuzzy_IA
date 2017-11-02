import biblio_fuzzy as bf

CONJUNTO_DURACION = ("T_Corto", "T_Regular", "T_Largo")
CONJUNTO_ESTRATEGIA = ("E_Minima", "E_Normal", "E_Maxima")
CONJUNTO_ACCION = ("A_Escasa", "A_Normal", "A_Excesiva")
CONJUNTO_DIFICULTAD = ("D_Facil", "D_Normal", "D_Experto")
CONJUNTO_EXPLORACION = ("X_Pequeño", "X_Normal", "X_Extenso")
CONJUNTO_SANGRE = ("S_Nada", "S_Normal", "S_Mucha")
#CONJUNTO_JUEGOS = ("RPG", "Disparos", "Peleas", "Plataformas")
CONJUNTO_RPG = ("T_Largo", "E_Maximo", "D_Experto", "Exploracion")
CONJUNTO_PLATAFORMAS = ("D_Experto", "Exploracion", "E_Normal", "T_Regular", "Accion")
CONJUNTO_PELEAS = ("T_Regular", "D_Normal", "Sangre", "E_Minima", "Accion")
CONJUNTO_DISPAROS = ("Sangre", "E_Minima", "Accion", "D_Facil", "T_Corto")

class SistemaFuzzyJuegos:
    def __init__(self):
        self.nivs_mem_duracion = [0, 0, 0]
        self.nivs_mem_estrategia = [0, 0, 0]
        self.nivs_mem_accion = [0, 0, 0]
        self.nivs_mem_dificultad = [0, 0, 0]
        self.nivs_mem_exploracion = [0, 0, 0]
        self.nivs_mem_sangre = [0, 0, 0]

    def pos_niv_mem_mayor(self, nivs_mem=list()):
        pos_mayor = 0
        for i in range(0, len(nivs_mem)):
            if nivs_mem[i] > nivs_mem[pos_mayor]:
                pos_mayor = i
        return pos_mayor
    
    def prod_membs_duracion(self, dato_nitido=0):        
        self.nivs_mem_duracion[0] = bf.curva_z(dato_nitido, 25, 50)
        self.nivs_mem_duracion[1] = bf.triangular_suave(dato_nitido, 25, 50, 75)
        self.nivs_mem_duracion[2] = bf.curva_s(dato_nitido, 50, 75)        

    def prod_membs_estrategia(self, dato_nitido=0):
        self.nivs_mem_estrategia[0] = bf.curva_z(dato_nitido, 25, 50)
        self.nivs_mem_estrategia[1] = bf.triangular_suave(dato_nitido, 25, 50, 75)
        self.nivs_mem_estrategia[2] = bf.curva_s(dato_nitido, 50, 75)
    
    def prod_membs_accion(self, dato_nitido=0):
        self.nivs_mem_accion[0] = bf.curva_z(dato_nitido, 25, 50)
        self.nivs_mem_accion[1] = bf.triangular_suave(dato_nitido, 25, 50, 75)
        self.nivs_mem_accion[2] = bf.curva_s(dato_nitido, 50, 75)
    
    def prod_membs_dificultad(self, dato_nitido=0):
        self.nivs_mem_dificultad[0] = bf.curva_z(dato_nitido, 25, 50)
        self.nivs_mem_dificultad[1] = bf.triangular_suave(dato_nitido, 25, 50, 75)
        self.nivs_mem_dificultad[2] = bf.curva_s(dato_nitido, 50, 75)        

    def prod_membs_exploracion(self, dato_nitido=0):
        self.nivs_mem_exploracion[0] = bf.curva_z(dato_nitido, 25, 50)
        self.nivs_mem_exploracion[1] = bf.triangular_suave(dato_nitido, 25, 50, 75)
        self.nivs_mem_exploracion[2] = bf.curva_s(dato_nitido, 50, 75)

    def prod_membs_sangre(self, dato_nitido=0):
        self.nivs_mem_sangre[0] = bf.curva_z(dato_nitido, 25, 50)
        self.nivs_mem_sangre[1] = bf.triangular_suave(dato_nitido, 25, 50, 75)
        self.nivs_mem_sangre[2] = bf.curva_s(dato_nitido, 50, 75)

    def fuzzificador_duracion(self, dato_nitido):
        conjunto = ""
        self.prod_membs_duracion(dato_nitido)
        conjunto = CONJUNTO_DURACION[self.pos_niv_mem_mayor(self.nivs_mem_duracion)]
        return conjunto
    
    def fuzzificador_estrategia(self, dato_nitido):
        conjunto = ""
        self.prod_membs_estrategia(dato_nitido)
        conjunto = CONJUNTO_ESTRATEGIA[self.pos_niv_mem_mayor(self.nivs_mem_estrategia)]
        return conjunto
    
    def fuzzificador_accion(self, dato_nitido):
        conjunto = ""
        self.prod_membs_accion(dato_nitido)
        conjunto = CONJUNTO_ACCION[self.pos_niv_mem_mayor(self.nivs_mem_accion)]
        if conjunto == "A_Normal" or conjunto == "A_Execisa":
            conjunto = "Accion"
        else:
            conjunto = "No_Accion"
        return conjunto
    
    def fuzzificador_dificultad(self, dato_nitido):
        conjunto = ""
        self.prod_membs_dificultad(dato_nitido)
        conjunto = CONJUNTO_DIFICULTAD[self.pos_niv_mem_mayor(self.nivs_mem_dificultad)]
        return conjunto
    
    def fuzzificador_exploracion(self, dato_nitido):
        conjunto = ""
        self.prod_membs_exploracion(dato_nitido)
        conjunto = CONJUNTO_EXPLORACION[self.pos_niv_mem_mayor(self.nivs_mem_exploracion)]
        if conjunto == "X_Normal" or conjunto == "X_Extenso":
            conjunto = "Exploracion"
        else:
            conjunto = "No_Exploracion"
        return conjunto
    
    def fuzzificador_sangre(self, dato_nitido):
        conjunto = ""
        self.prod_membs_sangre(dato_nitido)
        conjunto = CONJUNTO_SANGRE[self.pos_niv_mem_mayor(self.nivs_mem_sangre)]
        if conjunto == "S_Normal" or conjunto == "S_Mucha":
            conjunto = "Sangre"
        else:
            conjunto = "No_Sangre"
        return conjunto

    def calc_pertenencia_genero(self, genero=tuple(), caracteristicas=list()):
        puntos = 0
        for i in caracteristicas:
            if i in genero:
                puntos += 1
        return puntos/len(genero)

    def inferir_atributos_difusos_cualitativos(self, duracion="", estrategia="", accion="", 
                                                dificultat="", exploracion="", sangre=""):
        caracteristicas = [duracion, estrategia, accion, dificultat, exploracion, sangre]
        pert_genero = {"RPG": 0, "Plataformas": 0, "Peleas": 0, "Disparos": 0}
        
        pert_genero["RPG"] = self.calc_pertenencia_genero(CONJUNTO_RPG, caracteristicas)
        pert_genero["Plataformas"] = self.calc_pertenencia_genero(CONJUNTO_PLATAFORMAS, caracteristicas)
        pert_genero["Peleas"] = self.calc_pertenencia_genero(CONJUNTO_PELEAS, caracteristicas)
        pert_genero["Disparos"] = self.calc_pertenencia_genero(CONJUNTO_DISPAROS, caracteristicas)

        pert_mayor = "RPG"
        for key in pert_genero.keys():
            if pert_genero.get(key) > pert_genero.get(pert_mayor):
                pert_mayor = key

        return pert_mayor
