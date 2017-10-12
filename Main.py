from BiblioFuzzy import FuncMembresia as fm, OpLogFuzzy as opl, ImplFuzzy as imp

if __name__=='__main__':
    print('Biblioteca Fuzzy'.upper())  
    print('Prueba de funciones de membresia'.center(80, '#'))
    
    print('Trapecio Abierto Derecha a=5 y b=8'.center(60, '-'))
    for x in range(1, 15):
        print('Para u={:2d} tiene como salida={:.1f}'.format(x, fm.trapecio_abierto_der(x, 5, 8)))  
    
    print('Trapecio Abierto Izquierda a=5 y b=8'.center(60, '-'))
    for x in range(1, 15):
        print('Para u={:2d} tiene como salida={:.1f}'.format(x, fm.trapecio_abierto_izq(x, 5, 8)))

    print('Triangular a=5, b=8, c=11'.center(60, '-'))
    for x in range(1, 15):
        print('Para u={:2d} tiene como salida={:.1f}'.format(x, fm.triangular(x, 5, 8, 11)))
    
    print('Trapezoidal a=5, b=6, c=10, d=12'.center(60, '-'))
    for x in range(1, 15):
        print('Para u={:2d} tiene como salida={:.1f}'.format(x, fm.trapezoidal(x, 5, 6, 10, 12)))
    
    print('Curva S a=5, b=10'.center(60, '-'))
    for x in range(1, 15):
        print('Para u={:2d} tiene como salida={:.1f}'.format(x, fm.curva_s(x, 5, 10)))

    print('Curva Z a=5 y b=10'.center(60, '-'))
    for x in range(1, 15):
        print('Para u={:2d} tiene como salida={:.1f}'.format(x, fm.curva_z(x, 5, 10)))
    
    print('Triangular Suave a=5, b=8 y c=11'.center(60, '-'))
    for x in range(1, 15):
        print('Para u={:2d} tiene como salida={:.1f}'.format(x, fm.triangular_suave(x, 5, 8, 11)))
    
    print('Trapezoidal Suave a=5, b=7, c=10, y d=12'.center(60, '-'))
    for x in range(1, 15):
        print('Para u={:2d} tiene como salida={:.1f}'.format(x, fm.trapezoidal_suave(x, 5, 7, 10, 12)))
    
    print('Prueba de Operadores Logicos Fuzzy'.center(80, '#'))
    print('Compuerta AND'.center(60, '-'))
    for x in range(0, 2):
        for y in range(0, 2):
            print('Para {:.1f} AND {:.1f} -> {:.1f}'.format(x, y, opl.comp_and(x, y)))
    
    print('Compuerta OR'.center(60, '-'))
    for x in range(0, 2):
        for y in range(0, 2):
            print('Para {:.1f} AND {:.1f} -> {:.1f}'.format(x, y, opl.comp_or(x, y)))
    
    print('Niega'.center(60, '-'))
    for x in range(0, 2):        
        print('Para {:.1f} -> {:.1f}'.format(x, opl.niega(x)))
    
    print('Prueba de Implicacion Fuzzy'.center(80, '#'))
    print('Implicacion Zadeh'.center(60, '-'))
    for x in [p/10 for p in range(0, 11, 5)]:
        for y in [p/10 for p in range(0, 11, 5)]:
            print('Para ma_x={:.1f} , mb_y{:.1f} -> {:.1f}'.format(x, y, imp.implica_zadeh(x, y)))

    print('Implicacion Mamdani'.center(60, '-'))
    for x in [p/10 for p in range(0, 11, 5)]:
        for y in [p/10 for p in range(0, 11, 5)]:
            print('Para ma_x={:.1f} , mb_y{:.1f} -> {:.1f}'.format(x, y, imp.implica_mamdani(x, y)))
    
    print('Implicacion Godel'.center(60, '-'))
    for x in [p/10 for p in range(0, 11, 5)]:
        for y in [p/10 for p in range(0, 11, 5)]:
            print('Para ma_x={:.1f} , mb_y{:.1f} -> {:.1f}'.format(x, y, imp.implica_godel(x, y)))