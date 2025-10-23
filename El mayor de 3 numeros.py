#Programa para validar cual es el numero mayor entre 3 números.

num1 = float(input("introduce el primer numero:"))
num2 = float(input("introduce el segundo numero:"))
num3 = float(input("introduce el tercer numero:"))

if num1>= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

    print(f"El numero mayor es: {mayor}")