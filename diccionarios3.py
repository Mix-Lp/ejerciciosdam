frutas = {"manzana": 2.3, "kiwi": 4.5, "platano": 2.2}
prompt = "> "

print("Introduce una fruta")

key = input(prompt)

if frutas.get(key):

    print("Introduce los kilos que vas a comprar")
    weight = input(prompt)
    print("El precio total sera de %.2f euros." %
          (frutas.get(key)*int(weight)))
else:
    (
        print("No se ha encontrado dicha fruta.")
    )
