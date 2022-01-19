divisa = {"Euro": "€", "Dollar": "$", "Yen": "¥"}

prompt = "> "

print("Introduce una divisa para mostrar su simbolo: ")

rep = input(prompt)

print(divisa.get(rep,"No se ha encontrado la divisa especificada"))