prompt = "> "
password = "eureka"
print("Introduce la contraseña:")
userpass = input(prompt)
if password == userpass.lower():
    print("Contraseña correcta.")
else:
    print("ERROR: Contrasenia incorrecta")
