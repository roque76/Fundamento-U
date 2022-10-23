a = int(input('Ingresar valor de "a" en la formula: '))
b = int(input('Ingresar valor de "b" en la formula: '))
c = int(input('Ingresar valor de "c" en la formula: '))

if (pow(b,2)-4*a*c)<0:
    print('El resultado genera imaginarios.')
else:
    r_pos =(-b+sqrt(pow(b,2)-4*a*c))/2*a
    r_neg =(-b-sqrt(pow(b,2)-4*a*c))/2*a

print(f'Las respuestas son: {r_pos}, {r_neg} ')
