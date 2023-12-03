"""
Noms: Jofre Aleman, Dani Arco, Izan Arnaiz
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

# Control de errores
try:
    # Programa que calcula la altura y el ancho de un triángulo
    altura = int(input("Altura del triángulo (entre 2 y 9): "))
    if 2 <= altura <= 9:
        for i in range(1, altura + 1):
            print(i, end=" ")
            if i > 1 and i < altura:
                espacios = 2 * (i - 2)
                print(" " * espacios + str(i), end=" ")
            elif i == altura:
                print((str(i) + ' ') * (i-1), end="")
            print()
    else:
        print("La altura debe estar entre 2 y 9.")

except ValueError:
    print("Introduce un valor válido.")
finally:
    print("Programa terminado.")