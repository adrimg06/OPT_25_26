def configurar_servidor() -> None:
    servidor = {
        "ip": "192.168.1.10",
        "puerto": 80,
        "estado": "activo"
    }

    servidor["protocolo"] = "HTTPS"
    servidor.pop("estado")

    for clave, valor in servidor.items():
        print(f" {clave} : {valor}")



configurar_servidor()