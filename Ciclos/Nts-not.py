est= int(input('Ingresar cantidad de estudiantes: '))

while (i < est):
    
    i=0
    n_est= str(input('Ingresar nombre de estudiante: '))

    n1=float(input('\nIngresar nota1: '))
    n2=float(input('\nIngresar nota2: '))
    n3=float(input('\nIngresar nota3: '))
    n4=float(input('\nIngresar nota4: '))

    pr_n=((n1+n2+n3+n4)/4)
    if pr_n >=7 and pr_n<9:
        print(f'El estudiante {n_est} es notable con una nota de: {pr_n}')
    else:
        print('Estudiante no notable.')

    i=i+1