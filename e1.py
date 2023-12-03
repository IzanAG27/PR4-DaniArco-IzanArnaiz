"""
Noms: Jofre Aleman, Dani Arco, Izan Arnaiz
Data: 1/12/2023
Lliurament: 4/12/2023
ASIXc M03-UF1 A4 PR4

Descripció: Programa que demana a l'usuari la introducció de 10 nombres sencers
(que també podrien ser 10000000 😱😳😈) i ha de mostrar, al final i per pantalla,
quants són positius, quants negatius i quants zero.
"""

# Control de errores
try:

    # Variables para guardar información
    numero = input().split()
    longuitud = len(numero)
    positiu = 0
    negatiu = 0
    casSigui0 = 0
    cont = 0

    # Programa que calcula a través de les variables cuantos números són, positius, negatius o zero.
    if longuitud == 10:
        while cont != longuitud:
            if int(numero[cont]) > 0:
                positiu += 1
            elif int(numero[cont]) < 0:
                negatiu += 1
            elif int(numero[cont]) == 0:
                casSigui0 += 1
            else:
                print("Dades incorrectes, torna a provar amb un enter")
            cont += 1
        print("Números positius: {}\n\nNúmeros negatius: {}\n\nNúmeros igual a 0: {}".format(positiu, negatiu, casSigui0))
    else:
        print("La longuitud debe ser igual a 10 y solamente numeros enteros")
except ValueError:
    print("Introduce bien los datos")
finally:
    print("\nPrograma terminado")