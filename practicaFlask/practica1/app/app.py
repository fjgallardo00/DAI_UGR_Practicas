#./app/app.py
import re
from flask import Flask, url_for, redirect, render_template
app = Flask(__name__)
          
@app.route('/')
def helloworld():
  print("Hola mundo!")

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for("static", filename='page_not_found.html'))

@app.route('/fibonacci/<int:numero>')
def fibonacci(numero):
  return str(sucesion_fibonacci(numero))

@app.route('/eratostenes/<int:numero>')
def eratostenes(numero):
  return str(criba_eratostenes(numero))

@app.route('/expresiones_regulares/<cadena>')
def expresiones_regulares(cadena):

  if(RE_numero(cadena)):
    return str(True)
  
  if(RE_correo(cadena)):
    return str(True)

  if(RE_palabra(cadena)):
    return str(True)

  return str(False)

@app.route('/corchetes/<cadena>')
def corchetes(cadena):
  return str(is_corchetes_balanced(cadena))

@app.route('/imagen')
def imagen():
  return redirect(url_for("static", filename='index.html')) # Hacer html con el css para mostrarlo

def sucesion_fibonacci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return sucesion_fibonacci(n-1) + sucesion_fibonacci(n-2)

def criba_eratostenes(n):
  lista = []
  for i in range(2, n+1):
    lista.append(i)
  for i in range(2, n+1):
    for j in range(2, n+1):
      if i*j in lista:
        lista.remove(i*j)
  return lista

def is_corchetes_balanced(corchetes):
  corchete_abierto = "["
  corchete_cerrado = "]"
  pila = []

  for i in corchetes: 
    if i in corchete_abierto: 
      pila.append(i) 
 
    elif i in corchete_cerrado: 
      pos = corchete_cerrado.index(i) 
      if ((len(pila) > 0) and (corchete_abierto[pos] == pila[len(pila) -1])): 
        pila.pop()
      else:
        return False

    if len(pila) == 0:
      return True
    else:
      return False

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