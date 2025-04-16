def leap_year():
    a = int(input("Ingrese un año: "))
    b = a % 4
    c = a % 400
    d = a % 100
    if (b == 0 and d != 0) or c == 0: 
        print(f"El año {a} es bisiesto")
    else: 
        print(f"El año {a} no es bisiesto")
