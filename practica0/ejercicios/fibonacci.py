def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

fichero = open('fibonacci.txt', 'r')
numero = int(fichero.read())

resultado = fibonacci(numero)

fichero2 = open('fibonacci_salida.txt', 'w')
fichero2.write(str(resultado))