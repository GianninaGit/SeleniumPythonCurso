print("hello")

# comentarios

# variables, no hace falta aclarar qué tipo de dato es:
a = 3
print(a)

# strings
str = "Hello World"
print(str)

# escribí 3 variables y se asignan respectivamente a cada valor, ahorro lineas
b, c, d = 5, 6.4, "Great"
print(b)
print(c)
print(d)

# COMBINAR DATOS: esto da error: print("Value is " + b). Sí se puede concatenar variables de mismos tipos de datos.
# OK:
print("{} {}".format("Value is", b))

#para saber qué tipo de dato es una variable
print(type(c))


