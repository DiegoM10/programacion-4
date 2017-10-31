def generar_secuencias():
    numero = 1
    while True:
        yield numero
        numero = numero +2
if __name__== "__main__":

    numeros = generar_secuencias()
    for n in numeros:
        print(n)
        if n > 14:
            break