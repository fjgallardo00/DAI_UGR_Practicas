def criba_eratostenes(n):
  lista = []
  for i in range(2, n+1):
    lista.append(i)
  for i in range(2, n+1):
    for j in range(2, n+1):
      if i*j in lista:
        lista.remove(i*j)
  return lista
  
print(criba_eratostenes(100))