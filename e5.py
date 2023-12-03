"""
Noms: Jofre Aleman, Dani Arco, Izan Arnaiz
Data: 1/12/2023
Lliurament: 4/12/2023
ASIXc M03-UF1 A4 PR4

Descripció: Programa que realitza la multiplicació, de dos nombres sencers,  mitjançant sumes.
"""
try:

    numeros = input("").split()
    num1 = int(numeros[0])
    num2 = int(numeros[1])
    for x in range(num2):
        if x == num2 - 1:
            print(num1, end="")
        else:
            print(num1, " +  ", end="")
    print(" =",num1 * num2)

except ValueError:
    print("\nIntroduce bien los datos")
finally:
    print("\nPrograma terminado")