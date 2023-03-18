def is_balanceado(corchetes):
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

print(is_balanceado("[][][[[]]]"))
print(is_balanceado("[]"))