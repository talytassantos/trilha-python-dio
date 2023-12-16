numero = input("Informe um numero: ")

print(f"Essa é a tabuada do {numero}")

for numero in range(0, (int(numero)* 10)+ 1 , int(numero)):
    print (numero, end=" ")