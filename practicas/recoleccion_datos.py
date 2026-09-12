"""
Ejercicio 1

Lo primero es cumplir con el script de recoleccion de datos usando
todos los tipos de datos vistos en clase.

Tengo entendido que para el experimento se suele calcular tanto la carga
como el radio de la gota.
Viendo la fórmula de la carga, me imagino que primero calcula el radio para saber la masa de las gotitas
El código se basará en eso
"""

print("Programa para calcular la carga del electrón a partir del experimento de Milikan  \n")
print("Autor: Enrique Rodríguez Ramírez")

#Hay algunos valores que no se necesitan pedir al usuario
g = 9.78        #Asumiendo que estamos en cdmx, m/s^2
rho_aceite = 920    # Kg/m^3
rho_aire = 1.225    #kg/m^3
eta = 1.82e-5      #Pa s, viscosidad del aire

print("A continuación, ingrese las condiciones iniciales del experimento")

#Para calcular el campo entre dos placas ocupamos E = V/d
voltaje = float(input("Ingrese el voltaje aplicado en [V]: "))
d_placas = float(input("Ingrese la distancia entre las placas en [m]: \n"))

E = voltaje / d_placas

#Guardare esto en una tupla porque el ejercicio lo pide
condiciones = (voltaje, d_placas, E)

#Ahora haré listas que usaré para almacenar datos

cargas = []
radios = []
vel_ter = []    #Velocidades terminales de las gotas


"""Nota: Esto lo estoy pensando como que ya se tomaron los datos y solo es registrarlos en la computadora, 
i.e., ya sabes cuantos datos tienes."""


# Numero de gotas
n_gotas = int(input("Cuántas gotas se midieron? \n"))

print(f"Ahora ingrese los valores obtenidos para las velocidades terminales de cada gota \n")
print(f"Primero ingrese los valores sin campo eléctrico y luego con campo eléctrico")

#Ahora si viene el ciclo que hará toda la magia

for i in range(n_gotas):
    print (f"Gota número {i+1}")

    sin_E = float(input("Velocidad terminal sin campo electrico [m/s]: "))
    con_E = float(input("Velocidad terminal con campo electrico [m/s]: "))

    #Guardar velocidades en la lista
    vel_ter.append((sin_E, con_E))

    #Comenzamos haciendo la fórmula del radio de la gota.
    #La fórmula es raiz ( 9 eta nu / 2g (rho aceite - rho aire))

    # Radio de la gota
    radio = math.sqrt((9*eta*sin_E) / (2*g*(rho_aceite - rho_aire)))

    #Guardar radios en la lista
    radios.append(radio)

    # Ahora va la fórmula de la carga de la gota, q = (vol. esfera) por densidad del liquido por g / E
    v_esfera = (4/3)*math.pi*(radio**3)
    carga = v_esfera * rho_aceite * g / E

    #Guardar carga en la lista
    cargas.append(carga)

    print("El radio de la gota es:", radio, "[m]")
    print("Carga de la gota:", carga, "[C]")

#Ahora hacemos lo que pide del set para tener valores únicos
cargas_2 = set(cargas)

# Verificamos que las cargas sean positivas, pues hasta ahora deberian serlo, no? 
# #a menos que del campo electrico venga un signo negativo, pero eso debería compensarse con un cambio de signo en la velocidad
#I.E. según yo esto se corrige solo en el experimento, por lo que un negativo implica un error al inicio como masa negativa, creo.
cargas_3 = True   #El booleano que se pedía

for carga in cargas:
    if carga <= 0:
        cargas_3 = False

#Ahora pasamos a la sección B del código que es hacer una función, me falta un poco más de tiempo para hacer mejor esta transición
#me quede sin ideas sin que se vea forzado el meter así nadamas la función

#Voy a ocupar otras dos listas para guardar los datos
valores_n = []
estimaciones_e = []

def estimar_carga_electron(cargas_medidas):

    #Primera aproximacion de e
    e_aproximada = min(cargas_medidas)

    for carga in cargas_medidas:
        n = round(carga / e_aproximada)
        e_individual = carga / n    #El paso dos y 3 de las notas

        valores_n.append(n)
        estimaciones_e.append(e_individual) #Guardamos todo

    #Promedio
    e_promedio = sum(estimaciones_e) / len(estimaciones_e)

    #Desviacion estandar
    suma = 0

    #Ahora calculamos el promedio y su respectiva incertidumbre que es la desviacion estandar en este caso
    for e in estimaciones_e:
        suma += (e-e_promedio)**2

    desviacion = math.sqrt(suma / len(estimaciones_e))

    return e_promedio, desviacion


# Valor aceptado
e_aceptada = 1.602176634e-19

# Estimacion
e_estimado, desviacion = estimar_carga_electron(cargas)

# Error relativo
error = error_relativo(e_estimado, e_aceptada)

# --------------------------------------------------
# RESUMEN
# --------------------------------------------------

resumen = {
    "condiciones": condiciones,
    "cargas_medidas": cargas,
    "cargas_unicas": cargas_2,
    "cargas_validas": cargas_3,
    "carga_electron_estimada": e_estimado,
    "desviacion_estandar": desviacion,
    "error_relativo": error
}


""" 
Creo que ya no me da tiempo de entregar la parte de generar el .txt por la hora. 
Así que lo dejaré así en el repositorio.
El fin de semana pienso acabarlo de todos modos porque aún no le entiendo al 100 A GitHub,
pero si me pueden calificar aunque sea esta parte así como está sería increible.

Mis códigos de los otros ejercicios están en el otro repositorio
"""
