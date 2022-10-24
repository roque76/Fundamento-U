opc = int(input('Elija su unidad: 1-C\n, 2-K\n, 3-F'))
if opc == 1:
    C= float(input('Ingresar temperatura "Celsius" : '))
    K=C+273.15
    F=(1.8*C)+32
    print(f'La temperatura en K es: {K}')
    print(f'La temperatura en F es: {F}')
elif opc == 2:
    K=float(input('Ingresar temperatura "Kelvin" : '))
    C=K-273.15
    F=((K-273.15)*1.8)+32
    print(f'La temperatura en C es: {C}')
    print(f'La temperatura en F es: {F}')
elif opc == 3:
    F=float(input('Ingresar temperatura "Farenheit" : '))
    C=(F-32)/1.8
    K=((F-32)/1.8)+273.15
    print(f'La temperatura en "Celsius" es: {C}')
    print(f'La temperatura en "Kelvin" es: {K}')
