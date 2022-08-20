#DATO DE ENTRADA PARA ALMACENAR EL VALOR DEL NIVEL DE AGUA

nivelAgua=int(input("Digita el nivel de agua: "))

#CONDICIONES MULTIPLES CON PYTHON

if (nivelAgua>=0 and nivelAgua<20):
    print(f'Peligro, el nivel de agua es de {nivelAgua}, el cual es muy bajo')
elif (nivelAgua>=20 and nivelAgua<400):
    print(f' el nivel del agua es de {nivelAgua}, el cual es optimo')
elif (nivelAgua>=400):
    print(f'Peligro, el nivel de agua es de {nivelAgua}, el cual es muy alto')
else:
    print("digita una opcion valida")