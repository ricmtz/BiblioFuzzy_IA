import biblio_fuzzy as bf

CONJUNTO_DURACION = ("T_Corto", "T_Regular", "T_Largo")
CONJUNTO_ESTRATEGIA = ("E_Minima", "E_Normal", "E_Maxima")
CONJUNTO_ACCION = ("A_Escasa", "A_Normal", "A_Excesiva")
CONJUNTO_DIFICULTAD = ("D_Facil", "D_Normal", "D_Experto")
CONJUNTO_EXPLORACION = ("X_Pequeño", "X_Normal", "X_Extenso")
CONJUNTO_SANGRE = ("S_Nada", "S_Normal", "S_Mucha")    
CONJUNTO_JUEGOS = ("RPG", "Disparos", "Peleas", "Plataformas")

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
        for i in range(len(0, nivs_mem)):
            if nivs_mem[i] > nivs_mem[pos_mayor]:
                pos_mayor = i
        return pos_mayor
    
    def prod_membs_duraccion(self, dato_nitido=0):        
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