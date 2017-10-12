from math import cos, pi

class FuncMembresia:
    """Funciones de membresia"""
    @staticmethod
    def trapecio_abierto_der(u, a, b):    
        if u > b:
            return 1.0
        elif u < a: 
            return 0.0
        elif a <= u and u <= b:
            return (u - a) / (b - a)
    
    @staticmethod
    def trapecio_abierto_izq(u, a, b):
        if u > b:
            return 0.0
        elif u < a:
            return 1.0
        elif a <= u and u <= b:
            return (b - u) / (b - a)

    @staticmethod
    def triangular(u, a, b, c):
        if u < a or u > c:
            return 0.0
        elif a <= u and u <b:
            return (u - a) / (b - a)
        elif b <= u and u <= c:
            return (c - u) / (c - b)
    
    @staticmethod
    def trapezoidal(u, a, b, c, d):
        if u < a or u > d:
            return 0.0
        elif b <= u and u <= c:
            return 1.0
        elif a <= u and u < b:
            return (u - a) / (b - a)
        elif c < u and u <= d:
            return (d - u) / (d - c)
    
    @staticmethod
    def curva_s(u, a, b):
        if u > b:
            return 1.0
        elif u < a:
            return 0
        elif a <= u and u <= b:
            return (1 + cos(((u - b) / (b - a)) * pi)) / 2.0
            
    @staticmethod
    def curva_z(u, a, b):
        if u > b:
            return 0.0
        elif u < a:
            return 1.0
        elif a <= u  and u <= b:
            return (1 + cos(((u -a) / (b - a)) * pi)) / 2.0
    
    @staticmethod
    def triangular_suave(u, a, b, c):
        if u < a or u > c:
            return 0.0
        elif a <= u and u < b:
            return (1 + cos(((u - b) / (b - a)) * pi)) / 2.0
        elif a <= u and u <= b:
            return (1 + cos(((b- u) / (c - b)) * pi)) / 2.0

    @staticmethod
    def trapezoidal_suave(u, a, b, c, d):
        if u < a or u > d:
            return 0.0
        elif b <= u and u <= c:
            return 1.0
        elif a <= u and u < b:
            return (1 + cos(((u - b) / (b - a)) * pi)) / 2.0
        elif c < u and u <= d:
            return (1 + cos(((c - u) / (d - c)) * pi)) / 2.0

class Apoyo:
    """Accesorios de Apoyo"""
    @staticmethod
    def min_v(a, b):
        if a < b:
            return a
        return b

    @staticmethod
    def max_v(a, b):
        if a > b:
            return a
        return b

class OpLogFuzzy:
    """Operadores Logicos Fuzzy"""
    @staticmethod
    def comp_and(ma_u, mb_u):
        return Apoyo.min_v(ma_u, mb_u)

    @staticmethod
    def comp_or(ma_u, mb_u):
        return Apoyo.max_v(ma_u, mb_u)

    @staticmethod
    def niega(ma_u):
        return 1.0 - ma_u     
    
class ImplFuzzy:
    """Implicacion Fuzzy"""
    @staticmethod
    def implica_zadeh(ma_x, mb_y):
        return Apoyo.max_v(Apoyo.min_v(ma_x, mb_y), OpLogFuzzy.niega(ma_x))

    @staticmethod
    def implica_mamdani(ma_x, mb_y):
        return Apoyo.min_v(ma_x, mb_y)

    @staticmethod
    def implica_godel(ma_x, mb_y):
        if ma_x < mb_y:
            return 1
        return mb_y