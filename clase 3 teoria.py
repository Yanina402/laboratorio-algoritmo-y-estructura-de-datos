# Práctica Método Index() 1
# Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"

palabra = "ordenador"
caracter = palabra[4]
print(caracter)




#2Práctica Método Index() 2
# Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:

# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

#frase = "en teoria la teoria de la practica son los mismos.En la practica no lo son."
#palabra = "practica"
#resultado = frase.index(palabra)
#print(resultado)

#3) Práctica Método Index() 3
# Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:

# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

#----------------------------------------

#texto = "En teoria, la teoria y la practica son los mismos. En la practica no lo son."
#indice = texto.rfind("practica")
#print(indice)

# Práctica Sub-Strings 1
# Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:

# "Controlar la complejidad es la esencia de la programación"

# Pista: "Controlar" tiene un largo de 9 caracteres.

#pista = "controlar la complejidad es la escencia de la programacion"
#primera_palabra = pista[:pista.find(" ")]
#print(primera_palabra)

 #Práctica Sub-Strings 2
# Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.

# "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

#frase = "nunca confies en un ordenador que no puedas lanzar por una ventana"
#tercer_caracter = frase[9:3:66]
#print(tercer_caracter)

# Práctica Sub-Strings 3
# Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.

# "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
#frase = "es genial trabajar con ordenadores.No discuten, lo recuerdan todo y no beben tu cerveza"
#frase_invertida = frase[::-1]
#print(frase_invertida)

#Practica metodos de string 1
#Imprime el siguienta texto en mayuscula,empleando el metodo especifico de string:

#texto = "aprender python es genial"
#texto_mayuscula = texto.upper()
#print(texto_mayuscula)

# Práctica Métodos de String 2
# Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
#lista_palabras = ["La","legibilidad","cuenta."]

#lista_palabras = ["la" , "legibilidad" , "cuenta."]
#resultado = " ".join(lista_palabras)
#print(resultado)

# Práctica Métodos de String 3
# Reemplaza en la siguiente frase:

# "Si la implementación es difícil de explicar, puede que sea una mala idea."

# los siguientes pares de palabras:

# "difícil" --> "fácil"

# "mala" --> "buena"

# y muestra en pantalla la frase con ambas palabras modificadas.



#frase = "Si la implementacion es dificil de explicar, puede que sea una mala idea."
#frase_modificada = frase.replace("dificil","facil").replace("mala","buena")
#print(frase_modificada)                                
                        

