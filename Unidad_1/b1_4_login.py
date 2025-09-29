usuario_correcto = "admin"
contraseña_correcta = "1234"

usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")

if usuario == usuario_correcto and contraseña == contraseña_correcta:
    print("Acceso concedido. ¡Bienvenido!")

else:
    print("acceso denegado. Usuario o contraseña incorrectos.")

