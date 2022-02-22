ItemsInCart = 0
# 2 items will be added to cart, si no hay 2, debo stop el script
if ItemsInCart != 2:  #raise Exception("Products Cart count not matching")
    pass

assert(ItemsInCart == 0) #para que la prueba pase debe cumplirse el assert, sino dara error

# cuando creo que el codigo puede fallar, pero no quiero que el caso se detenga, encierro el bloque en un TRY
# que se manda a un CATCH, donde se especifique un detalle del error.

try:
    print("1")
    raise Exception("mensaje de error")
    print("2")
except Exception as e:
    print(e)
finally:
    print("Finally")

# try:
    #     with open("archivoQueNoExiste.txt", 'r') as paraLeer:
#         paraLeer.read()
# except: #es como catch en otros lenguajes, doy un msj customizado del error
#     print("Hay un error en el block try")


# try:
    #     with open("archivoQueNoExiste.txt", 'r') as paraLeer:
#        paraLeer.read()
# except Exception as e:  # es como catch en otros lenguajes
#     print(e) #permite mostrar específicamente cual es el error
# finally:
#    print("cleaning up resources")