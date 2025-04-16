import math
def line():
    a = input("Ingrese el coeficiente A: ")
    a = float(a)
    b = input("Ingrese el coeficiente B: ")
    b = float(b)
    c = input("Ingrese el coeficiente X1: ")
    c = float(c)
    d = input("Ingrese el coeficiente X2: ")
    d = float(d)

    print(f"El coeficiente A de su ecuación de la recta es: {a}")
    print(f"El coeficiente B de su ecuación de la recta es: {b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {c}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {d}")
    print("\nPara la siguiente ecuación:")
    print(f"\tY = {a}X + {b}")
    print("\nDados los siguientes puntos:")
    y1 = a*c + b
    y2 = a*d + b
    print(f"\tP1 ({c}, {y1})")
    print(f"\tP2 ({d}, {y2})")
    p1 = [c, y1]
    p2 = [d, y2]
    distance = math.dist(p1, p2)
    
    print(f"\nLa distancia entre ellos es: {distance}")
