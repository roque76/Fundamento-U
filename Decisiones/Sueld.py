h = float(input('Ingrear la cantidad de horas trabajadas: '))
tar = float(input('Ingresar tarifa por hora trabajada: '))
suel= h*tar
seg = suel*0.8
suel_t=seg+suel

if seg<300:
    b=suel_t*0.2
    suel_t=suel_t+b
    print(f'El salario total es: {suel_t}')
else: 
    print(f'El salario total es: {suel_t}')