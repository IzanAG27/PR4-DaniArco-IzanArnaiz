"""
Noms: Jofre Aleman, Dani Arco, Izan Arnaiz
Data: 1/12/2023
Lliurament: 4/12/2023
ASIXc M03-UF1 A4 PR4

Descripció:
Programa que mostra per pantalla la suma de tots els nombres senars i de tots els nombres parells inferiors a
un número límit, que l’usuari introdueix per teclat.
 Ex: 	si el límit és 31 sumaParells 240 i sumaSenars 225
si el límit és 54 sumaParells 702 i sumaSenars 729
"""
try:
    num = int(input())

    sumaP = 0
    sumaS = 0

#S'utikitza el if per poder diferenciar entre senars i parells, d'aquesta manera podem assignar els numeros
#senars i parells a cada suma per poder sumar-li el segunet numero
    for i in range(num):
        if i % 2 == 0:
            sumaP += i
        else:
            sumaS += i

    print(f'Si el límit és {num}, la sumaParells és {sumaP} i la sumaSenars {sumaS}')

except ValueError:
    print("Introduce bien los datos")
finally:
    print("Programa terminado")