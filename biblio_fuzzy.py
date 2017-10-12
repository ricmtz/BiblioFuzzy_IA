from math import cos, pi

#Funciones de membresia    
def trapecio_abierto_der(u, a, b):    
    if u > b:
        return 1.0
    elif u < a:
        return 0.0
    elif a <= u and u <= b:
        return (u - a) / (b - a)

def trapecio_abierto_izq(u, a, b):
    if u > b:
        return 0.0
    elif u < a:
        return 1.0
    elif a <= u and u <= b:
        return (b - u) / (b - a)

def triangular(u, a, b, c):
    if u < a or u > c:
        return 0.0
    elif a <= u and u < b:
        return (u - a) / (b - a)
    elif b <= u and u <= c:
        return (c - u) / (c - b)

def trapezoidal(u, a, b, c, d):
    if u < a or u > d:
        return 0.0
    elif b <= u and u <= c:
        return 1.0
    elif a <= u and u < b:
        return (u - a) / (b - a)
    elif c < u and u <= d:
        return (d - u) / (d - c)

def curva_s(u, a, b):
    if u > b:
        return 1.0
    elif u < a:
        return 0
    elif a <= u and u <= b:
        return (1 + cos(((u - b) / (b - a)) * pi)) / 2.0

def curva_z(u, a, b):
    if u > b:
        return 0.0
    elif u < a:
        return 1.0
    elif a <= u  and u <= b:
        return (1 + cos(((u -a) / (b - a)) * pi)) / 2.0

def triangular_suave(u, a, b, c):
    if u < a or u > c:
        return 0.0
    elif a <= u and u < b:
        return (1 + cos(((u - b) / (b - a)) * pi)) / 2.0
    elif b <= u and u <= c:
        return (1 + cos(((b- u) / (c - b)) * pi)) / 2.0

def trapezoidal_suave(u, a, b, c, d):
    if u < a or u > d:
        return 0.0
    elif b <= u and u <= c:
        return 1.0
    elif a <= u and u < b:
        return (1 + cos(((u - b) / (b - a)) * pi)) / 2.0
    elif c < u and u <= d:
        return (1 + cos(((c - u) / (d - c)) * pi)) / 2.0

#Accesorios de Apoyo
def min_v(a, b):
    if a < b:
        return a
    return b

def max_v(a, b):
    if a > b:
        return a
    return b

#Operadores Logicos Fuzzy
def comp_and(ma_u, mb_u):
    return min_v(ma_u, mb_u)

def comp_or(ma_u, mb_u):
    return max_v(ma_u, mb_u)

def niega(ma_u):
    return 1.0 - ma_u

#Implicacion Fuzzy"""
def implica_zadeh(ma_x, mb_y):
    return max_v(min_v(ma_x, mb_y), niega(ma_x))

def implica_mamdani(ma_x, mb_y):
    return min_v(ma_x, mb_y)

def implica_godel(ma_x, mb_y):
    if ma_x <= mb_y:
        return 1
    return mb_y
