asignaturas = ["Fisica", "Quimica", "Matematicas", "Historia", "Lengua"]

print(asignaturas)

for i in asignaturas:
    (
        print("Yo estudio %s" % i)
    )


asignaturas3 = asignaturas+asignaturas

print(asignaturas3)

asignaturasSet = set(asignaturas3)

print(asignaturasSet)
