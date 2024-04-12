def tabla(numero):
    for x in range(1,11):
        print(f"{numero}X{x}={numero*x}")

numero = int(input("que tabla quieres?"))
tabla(numero)