print('INICIO')

opc = int(input('(1=Mayor a Menor )-(2=Menor a Mayor)'))

n1= int(input('Ingrese el primer número: '))
n2 = int(input('Ingrese el segundo numero: '))
n3 = int(input('Ingrese el tercer numero'))

if opc == 1:
    if n1>n2 and n1>n3 and n2>n3:
        print(n1,n2,n3)
    elif n1>n2 and n1>n3 and n2<n3:
        print(n1,n3,n2)
    elif n2>n1 and n2>n3 and n1>n3:
        print(n2,n1,n3)
    elif n2>n1 and n2>n3 and n3>n1:
        print(n2,n3,n1)
    elif n3>n1 and n3>n2 and n2>n1:
        print(n3,n2,n1)
    elif n3>n1 and n3>n2 and n2<n1:
        print(n3,n1,n2)

if opc == 2:
    if n1>n2 and n1>n3 and n2>n3:
        print(n3,n2,n1)
    elif n1>n2 and n1>n3 and n2<n3:
        print(n2,n3,n1)
    elif n2>n1 and n2>n3 and n1>n3:
        print(n3,n1,n2)
    elif n2>n1 and n2>n3 and n3>n1:
        print(n1,n3,n2)
    elif n3>n1 and n3>n2 and n2>n1:
        print(n1,n2,n3)
    elif n3>n1 and n3>n2 and n2<n1:
        print(n2,n1,n3)