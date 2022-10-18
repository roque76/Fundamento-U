# tablas de multiplicar

tab = int(input('Ingresar valor de la primera tabla: '))
lim = int(input('Ingresar valor de la tabla final: '))
mult = int(input('Ingresar valor del multiplicador: '))

while tab<lim:
    tab = tab+1
    print('Inicio tabla #', tab,'\n')
    for x in range (mult+1):
        res = tab*x
        print(x,'*',tab,'=',res)
    print('Fin tabla #',tab,'\n')