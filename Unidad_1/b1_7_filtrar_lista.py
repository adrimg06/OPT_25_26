nombres = ["Ana", "Rody", "adrián", "Lucía", "andrés", "María", "Alma", "Jesus"]

for nombre in nombres:

    if nombre.startswith("A") or nombre.startswith("a"):
        continue

    print(nombre)
