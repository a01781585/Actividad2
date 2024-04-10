def decimal_a_binario(numero):
    return bin(numero)

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)