#RETO PARA LA CASA: hacer un programa que lea los dias del año, y segun el dia y mes que escriba, indique en que estacion estamos,
#SI SE HACE EL RETO, SE PUEDE NEGOCIAR EL EXAMEN

mes=input("Digita el mes: ")

#CONDICIONES MULTIPLES CON PYTHON

if (mes=='enero' or mes=='febrero' or mes=='marzo'):
    print(f'El mes de {mes}, hace parte de Invierno')
elif (mes=='julio' or mes=='agosto' or mes=='septiembre'):
    print(f'El mes de {mes}, hace parte de Verano')
elif (mes=='abril' or mes=='mayo' or mes=='junio'):
    print(f'El mes de {mes}, hace parte de Primavera')
elif (mes=='octubre' or mes=='noviembre' or mes=='diciembre'):
    print(f'El mes de {mes}, hace parte de Otoño')
else:
    print("digita una opcion valida")