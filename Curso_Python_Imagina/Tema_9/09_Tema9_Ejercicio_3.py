# A partir del siguiente código que calcula la suma parcial de cada elemento y después la total. 
# Crear uno equivalente con programación funcional


data = [[1,2], [3,4], [5,6]]
res1 = []
for item in data:
    res1.append(sum(item))
print(sum(res1))

suma_total = sum(map(lambda x : sum(x), data)) # Suma, map para recorrer elmentos de la lista, funcion lambda para sumar los elementos de la lista.
print(suma_total)