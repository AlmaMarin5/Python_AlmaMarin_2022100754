#crear un programa que pida dos numeros y obtenga como resultado cual de 
#cual de ellos es par o si ambos lo son
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Verificar cuáles son pares
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos números son pares.")
elif num1 % 2 == 0:
    print("Solo el primer número es par.")
elif num2 % 2 == 0:
    print("Solo el segundo número es par.")
else:
    print("Ninguno de los dos números es par.")