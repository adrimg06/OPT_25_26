def procesar_sensores() -> None:
    lecturas = [25.5, 30.2, -99, 27.8]

    it = iter(lecturas)
    elemento = next(it, None)
    error_detectado = False

    while elemento is not None:
        if elemento == -99:
            error_detectado = True
            break  # Salimos del bucle inmediatamente

        print(f"Lectura procesada: {elemento}")
        elemento = next(it, None)

    if error_detectado:
        print("Proceso interrumpido por error.")

procesar_sensores()