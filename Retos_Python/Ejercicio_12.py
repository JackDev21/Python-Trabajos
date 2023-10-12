
beatles = [] # paso 1
print("Paso 1:", beatles)

beatles.append("Jonh Lennon")
beatles.append ("Paul McCartney")
beatles.append ("George Harrison")

print("Paso 2:", beatles)

for i in range(1):
    beatles.append("Stu Sutcliffe")
    beatles.append("Pete Best") # paso 3
    
print("Paso 3:", beatles)

del beatles[3]
del beatles[-1] #paso 4

print("Paso 4:", beatles)

# paso 5
beatles.insert(0,"Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))
