def analizar_stock(producto_buscado: str) -> None:
    almacen = ["ratón", "teclado", "monitor", "ratón", "teclado", "ratón"]

    n_stock = almacen.count(producto_buscado)

    if n_stock > 2:
        print(f" Stock crítico de {producto_buscado}: {n_stock} unidades.")
    elif n_stock <= 2:
        print(f"stock aceptable de {producto_buscado} {n_stock} unidades.")
    else:
        print(f"El producto {producto_buscado} no esta en la lista")


analizar_stock("ratón")
analizar_stock("monitor")
analizar_stock("webcam")