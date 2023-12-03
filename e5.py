"""
Noms: Jofre Aleman, Dani Arco, Izan Arnaiz
Data: 1/12/2023
Lliurament: 4/12/2023
ASIXc M03-UF1 A4 PR4

Descripció: Programa que realitza la multiplicació, de dos nombres sencers,  mitjançant sumes.
"""

# Control de errores
try:

    # Programa que calcula las veces que una multiplicación multiplica a través de sumas
    num1, num2 = [int(x) for x in input().split()]

    # Si x es igual que num2 le resta 1 y le quita la str +, si no lo es, le añade el +
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