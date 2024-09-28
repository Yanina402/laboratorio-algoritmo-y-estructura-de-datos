texto =  input ("ingrese un texto")
print("excelente, ahora ingrese tres letras diferentes para mostrarme que puedo hacer con ello.")
letras_0 = input ("ingresa la primera letra:")
letras_1 = input ("ingresa la segunda letra:")
letras_2 = input ("ingresa la tercer letra:")

contar_1 = texto.count(letras_0)
contar_2 = texto.count(letras_1)
contar_3 = texto.count(letras_2)
print(f"la letra{letras_0} aparece {contar_1} veces")
print (f"la letra{letras_1} aparece {contar_2} veces")
print (f"la letra{letras_2} aparece {contar_3} veces")
 
palabras_texto = texto.split()
resultado_palabras = len(palabras_texto)
print(f"el texto que ingresaste tiene(resultado_palabras)")

inicio = texto[0]
fin = texto[-1] 
print(f"muestrame la primera letra del texto {texto[0]}")
print(f"muestrame la ultima letra del texto {texto[-1]}")

reverse = texto[::-1] 
print(f"mostrar en pantalla como quedaria el texto invertido:{texto[::-1]}")

palabra = "python"
if palabra in texto: 
print("la palabra 'python'se encuentra en el texto.")
else:
print("la palabra paython no se encuentra en el texto.")







    