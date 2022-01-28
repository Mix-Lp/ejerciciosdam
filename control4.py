prompt = "> "
print("Introduce un numero: ")
num1 = int(input(prompt))
print("Introduce otro numero:")
num2 = int(input(prompt))
if num2 == 0:
    print("Imposible dividir, el divisor es 0")
else:
    print("El resultado es %d" % (num1/num2))

