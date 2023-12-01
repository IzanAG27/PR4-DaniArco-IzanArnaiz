"""
Noms: Dani Arco, Izan Arnaiz
Data: 1/12/2023
Lliurament: 4/12/2023
ASIXc M03-UF1 A4 PR4

Descripció:
Programa que mostra un triangle amb nombres a les cantonades.  Cal demanar quina
alçada ha de tenir el triangle. Els valors permesos per a l'alçada son entre 2 i 9.
(ambdós inclosos)
INPUT
Alçada del triangle: 5
OUTPUT
1
2 2
3   3
4     4
5 5 5 5 5

"""
cont = " "
try:
    altura = int(input())

    for i in range(1, altura+1):
        print(i)
        if i == altura:
            print((str(i) + ' ') * i, end="")
            print()
        else:
            print(str(i+1) + cont, end="")
            cont = cont + " "

except ValueError:
    print("Introduce bien los datos")
finally:
    print("Programa terminado")