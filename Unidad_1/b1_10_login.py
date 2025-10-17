# Variables usuario
email_registrado = ""
password_registrada = ""

# Menu
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("[1] Registrarse")
    print("[2] Iniciar sesión")
    print("[3] Salir")
    opcion = input("Elige una de estas opciones: ")

    # OPCIÓN 1:REGISTARSE
    if opcion == "1":
        while True:
            email = input("Introduce tu correo electrónico: ")

            # email validación
            if len(email) < 3:
                print("El correo debe tener al menos 3 caracteres.")
            elif "@" not in email:
                print("El correo debe contener '@'.")
            elif not (".com" in email or ".es" in email or ".net" in email):
                print("El correo debe tener una extensión válida (.com, .es, .net).")
            elif any(sym in email for sym in "!#$%&*?,"):
                print("El correo no debe contener símbolos especiales (!#$%&*?, etc.).")
            else:
                email_registrado = email  # variables que deben de ser verdaderas para iniciar sesión
                break

        while True:
            password = input("Crea una contraseña: ")

            # Validaciones de la contraseña
            if len(password) < 8:
                print("La contraseña debe tener al menos 8 caracteres.")
            elif not any(c.isupper() for c in password):
                print("La contraseña debe tener al menos una letra mayúscula.")
            elif not any(c.isdigit() for c in password):
                print("La contraseña debe tener al menos un número.")
            elif not any(c in "!@#$%&*?," for c in password):
                print("La contraseña debe tener al menos un símbolo especial (!@#$%&*?, etc.).")
            else:
                password_registrada = password
                print("Registro completado con éxito.")
                break

    # OPCIÓN 2: inicio de sesión
    elif opcion == "2":
        if email_registrado == "":
            print(" No hay ningún usuario registrado. Regístrate primero.")
        else:
            email_login = input("Introduce tu correo electrónico: ")
            if email_login != email_registrado:
                print(" Usuario no existe.")
            else:
                intentos = 0
                while intentos < 3:
                    password_login = input("Introduce tu contraseña: ")
                    if password_login == password_registrada:
                        print(" Acceso concedido.")
                        break
                    else:
                        intentos += 1
                        print(" Contraseña incorrecta. Intentos restantes:", 3 - intentos)

                if intentos == 3:
                    print(" Demasiados intentos fallidos. Regresando al menú principal.")

    # OPCIÓN 3: SALIR
    elif opcion == "3":
        print(" Saliendo del programa...")
        break

    # OPCIÓN NULA
    else:
        print("Opción no válida. Elige 1, 2 o 3.")
