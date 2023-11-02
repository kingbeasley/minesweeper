import random

def crear_campo(filas, columnas, minas):
    campo = [[" " for _ in range(columnas)] for _ in range(filas)]
    minas_colocadas = 0

    while minas_colocadas < minas:
        x, y = random.randint(0, filas - 1), random.randint(0, columnas - 1)
        if campo[x][y] != "X":
            campo[x][y] = "X"
            minas_colocadas += 1

    return campo

def mostrar_campo(campo):
    filas = len(campo)
    columnas = len(campo[0])

    print("\n   ", end="")
    for col in range(columnas):
        print(f"{col} ", end="")
    print("\n")

    for fila in range(filas):
        print(f"{fila}  ", end="")
        for col in range(columnas):
            if campo[fila][col] == " ":
                print(".", end=" ")
            else:
                print(campo[fila][col], end=" ")
        print()

def contar_minas(campo, fila, col):
    filas = len(campo)
    columnas = len(campo[0])
    contador = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= fila + i < filas and 0 <= col + j < columnas:
                if campo[fila + i][col + j] == "X":
                    contador += 1

    return contador

def revelar_casilla(campo, fila, col):
    if campo[fila][col] == "X":
        return False
    elif campo[fila][col] == " ":
        campo[fila][col] = str(contar_minas(campo, fila, col))
    return True

def jugar_buscaminas(filas, columnas, minas):
    campo = crear_campo(filas, columnas, minas)
    mostrar_campo(campo)

    while True:
        fila = int(input("Ingrese la fila: "))
        col = int(input("Ingrese la columna: "))

        if not (0 <= fila < filas) or not (0 <= col < columnas):
            print("Coordenadas fuera de rango. Intente nuevamente.")
            continue

        if not revelar_casilla(campo, fila, col):
            mostrar_campo(campo)
            print("¡Has perdido!")
            break

        mostrar_campo(campo)

        casillas_sin_descubrir = sum(1 for fila in campo for casilla in fila if casilla == " ")
        if casillas_sin_descubrir == minas:
            print("¡Felicidades! Has ganado.")
            break

if __name__ == "__main__":
    filas = 8
    columnas = 8
    minas = 10
    jugar_buscaminas(filas, columnas, minas)
