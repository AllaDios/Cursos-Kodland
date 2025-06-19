ejemplo = open('ejemplo.txt', 'r',encoding='utf-8')
texto = ejemplo.read()
print(texto)
ejemplo.close()

ejemplo2 = open("instituto_tcnico_salesiano_villada_cover.jpg", "rb")
imagenes = ejemplo2.read()
print(imagenes)
ejemplo2.close()