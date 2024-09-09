from clases import Vehiculo, Automovil, AutomovilCarga, AutomovilPasajeros, Bicicleta, Motocicleta
from utilitarios import imprimir,guardar,recuperar,guardar_encabezado,obtenerEncabezados,datos_de_diccionario,obtenerListaEncabezados
##################################################################################################
print (' CREACION DE VEHICULO ')
##################################################################################################
vehiculo1 = Vehiculo("Toyota","Yaris",4)
datos = str(vehiculo1.Ver())
imprimir(" Vehiculo1 :",datos)
##################################################################################################
print (' CREACION DE AUTOMOVIL ')
##################################################################################################
automovil1 = Automovil("Toyota","Yaris",4, 160 , 1500)
datos = str(automovil1.Ver())
imprimir(" Automovil1 :", datos)
##################################################################################################
print (' CREACION DE AUTOMOVIL DE PASAJEROS ')
##################################################################################################
automovilPasajeros1 = AutomovilPasajeros("Ford","Fiesta",4, 180 , 1800,6)
datos = str(automovilPasajeros1.Ver())
imprimir(" AutomovilPasajeros1 :", datos)
##################################################################################################
print (' CREACION DE AUTOMOVIL DE CARGA ')
##################################################################################################
automovilCarga1 = AutomovilCarga("Chevrolet","Dmax",4, 180 , 2500, 20000)
datos = str(automovilCarga1.Ver())
imprimir(" AutomovilCarga1 :", datos)

##################################################################################################
print (' CREACION DE BICICLETA ')
##################################################################################################
bicicleta1 = Bicicleta("Bianchi","Spider",2 ,"Carrera")
datos = str(bicicleta1.Ver())
imprimir(" Bicicleta1 :", datos)

##################################################################################################
print (' CREACION DE MOTOCICLETA ')
##################################################################################################

motocicleta1 = Motocicleta("BMW","1200R",2 ,"OFFROAD", 21 ,"DobleT","4T")
datos = str(motocicleta1.Ver())
imprimir(" Motocicleta1 :",datos)
##################################################################################################
print (' COMPROBACION DE INSTANCIAMIENTOS ')
##################################################################################################
datos = " Motocicleta es Instancia con relacion a Vehiculo ",isinstance(motocicleta1,Vehiculo)
imprimir(" Clase Vehiculo :",datos)

datos = " Motocicleta es Instancia con relacion a Automovil ",isinstance(motocicleta1,Automovil)
imprimir(" Clase Automovil :",datos)

datos = " Motocicleta es Instancia con relacion a AutomovilPasajeros ",isinstance(motocicleta1,AutomovilPasajeros)
imprimir(" Clase AutomovilPasajeros :",datos)

datos = " Motocicleta es Instancia con relacion a AutomovilCarga ",isinstance(motocicleta1,AutomovilCarga)
imprimir(" Clase AutomovilCarga :",datos)

datos = " Motocicleta es Instancia con relacion a Bicicleta ",isinstance(motocicleta1,Bicicleta)
imprimir(" Clase Bicicleta :",datos)

datos = " Motocicleta es Instancia con relacion a Motocicleta ",isinstance(motocicleta1,Motocicleta)
imprimir(" Clase Motocicleta :",datos)


####################################################################################################
guardar_encabezado("vehiculosCarga.csv",obtenerEncabezados(automovilCarga1.__dict__.keys()))

lista_encabezados = obtenerListaEncabezados(automovilCarga1.__dict__.keys())

datos_imprimir = datos_de_diccionario(automovilCarga1.__dict__,lista_encabezados)

guardar("vehiculosCarga.csv",datos_imprimir)
print ('#########################################################################################')
print (' >>>> GENERACION DE ARCHIVO EN FORMATO CSV PARA VEHICULOS DE CARGA <<<<')
print ('#########################################################################################')

vehiculosCarga = recuperar("vehiculosCarga.csv")
##################################################################################################
print (' LISTADO VEHICULOS DE CARGA <<LEIDOS DESDE FORMATO CSV>>')
##################################################################################################
for automovil in vehiculosCarga:
    imprimir('vehiculosCarga ',automovil)

####################################################################################################
guardar_encabezado("vehiculosPasajeros.csv",obtenerEncabezados(automovilPasajeros1.__dict__.keys()))

lista_encabezados = obtenerListaEncabezados(automovilPasajeros1.__dict__.keys())

datos_imprimir = datos_de_diccionario(automovilPasajeros1.__dict__,lista_encabezados)

guardar("vehiculosPasajeros.csv",datos_imprimir)
print ('#########################################################################################')
print (' >>>> GENERACION DE ARCHIVO EN FORMATO CSV PARA VEHICULOS DE PASAJEROS <<<<')
print ('#########################################################################################')

vehiculosPasajeros = recuperar("vehiculosPasajeros.csv")
##################################################################################################
print (' LISTADO VEHICULOS DE PASAJEROS <<LEIDOS DESDE FORMATO CSV>>')
##################################################################################################
for automovil in vehiculosPasajeros:
    imprimir('vehiculosPasajeros ',automovil)


    
##################################################################################################
guardar_encabezado("vehiculos2ruedas.csv",obtenerEncabezados(motocicleta1.__dict__.keys()))

lista_encabezados = obtenerListaEncabezados(motocicleta1.__dict__.keys())

datos_imprimir = datos_de_diccionario(motocicleta1.__dict__,lista_encabezados)

guardar("vehiculos2ruedas.csv",datos_imprimir)


lista_encabezados = obtenerListaEncabezados(bicicleta1.__dict__.keys())

datos_imprimir = datos_de_diccionario(bicicleta1.__dict__,lista_encabezados)

guardar("vehiculos2ruedas.csv",datos_imprimir)
print ('#########################################################################################')
print (' >>>> GENERACION DE ARCHIVO EN FORMATO CSV PARA VEHICULOS DE DOS RUEDAS <<<<')
print ('#########################################################################################')

vehiculos2ruedas = recuperar("vehiculos2ruedas.csv")
##################################################################################################
print (' LISTADO VEHICULOS DE DOS RUEDAS (MOTO Y BICI)  <<LEIDOS DESDE FORMATO CSV>> ')
##################################################################################################
for vehiculos2r in vehiculos2ruedas:
    imprimir('Vehiculos 2 Ruedas ',vehiculos2r)
    #imprimir(" Archivo CSV : ",automovil)

