ejemplo = open("ejemplo.txt", "w")
text = input("Ingrese el texto a remplazar: ")
ejemplo.write(text)
ejemplo.close()

ejemplo2 = open("ejemplo.txt", "a")
text = input('Ingrese el texto a agregar: ')
ejemplo2.write(text)
ejemplo2.close()