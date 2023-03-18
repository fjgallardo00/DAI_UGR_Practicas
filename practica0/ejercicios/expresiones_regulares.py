import re

def RE_palabra(palabra):
    if (re.search('^[A-Za-z]+ ([A-Z]){1}$', palabra)):
        return True
    return False

def RE_correo(correo):
    if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', correo)):
        return True
    return False

def RE_numero(numero):
    if (re.search('^\d{4}(?:-|\s)\d{4}(?:-|\s)\d{4}(?:-|\s)\d{4}$', numero)):
        return True
    return False

palabra = "Apellido N"
correo = "ejemplo@gmail.org"
numero = "1234-5678-9012-3456"

print(palabra)
print(RE_palabra(palabra))

print(correo)
print(RE_correo(correo))

print(numero)
print(RE_numero(numero))
