prompt = "> "

print("Introduce tu nombre")
name = input(prompt)
print("Introduce tu edad")
age = input(prompt)
print("Introduce tu direccion")
location = input(prompt)
print("Introduce tu numero de telefono")
phone = input(prompt)

datos = {"nombre" : name, "edad" : age, "dir" : location, "number" : phone}



print("%s tiene %s años, vive en %s y su numero de telefono es %s" %(
    datos.get("nombre","Ni idea"),datos.get("edad","no lo se"),
    datos.get("dir","no lo se"),datos.get("number","no lo se")))