def mysplit(strng):
    # devolver [] si la cadena está vacía o solo contiene espacios en blanco
    if strng == '' or strng.isspace():
        return [ ]
    # preparar una lista a devolver
    lst = []
    # preparar una palabra para construir palabras subsecuentes
    word = ''
    # verificar si actualmente estamos dentro de una palabra (es decir, si la cadena comienza con una palabra)
    inword = not strng[0].isspace()
    # iterar a través de todos los caracteres en cadena
    for x in strng:
        # si actualmente estamos dentro de una cadena...
        if inword:
            # ... y el carácter actual no es un espacio...
            if not x.isspace():
                # ... actualizar palabra actual
                word = word + x
            else:
                # ... de lo contrario, llegamos al final de la palabra, por lo que debemos agregarla a la lista...
                lst.append(word)
                # ... y señalar que estamos ahora fuera de la palabra
                inword = False
        else:
            # si estamos fuera de la palabra y llegamos a un carácter no que no es un espacio en blanco...
            if not x.isspace():
                # ... significa que ha comenzado una nueva palabra, por lo que debemos recordarla y...
                inword = True
                # ... almacenar la primera letra de la nueva palabra
                word = x
            else:
                pass
    # si hemos dejado la cadena y hay una cadena no vacía en la variable word, necesitamos actualizar la lista
    if inword:
        lst.append(word)
    # devolver la lista al invocador
    return lst


print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
