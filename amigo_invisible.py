import random
from io import *

# Dar la bienvenida, introducir el primer presupuesto presupuesto e introducir el primer nombre

lista_presupuesto=[]
lista_jugadores=[]

print("\nBIENVENIDO AL AMIGO INVISIBLE\n")
while True:
	try:
		presupuesto = float(input("Por favor, introduce un presupuesto con un maximo de 15 euros: "))
		while presupuesto <= 0 or presupuesto > 15:
			print("Presupuesto equivocado, vuelve a intentarlo")
			presupuesto = float(input("Por favor, introduce un presupuesto con un maximo de 15 euros: "))
			break;
		else:
			lista_presupuesto.append(presupuesto)
			print("Tu presupuesto es de " + str(presupuesto) + " euros\n")
			break;
	except NameError:
		print("No se permiten letras, vuelve a intentarlo")

nombre_jugador=str(input("Escribe tu nombre: \n"))
lista_jugadores.append(nombre_jugador)
print("Tu nombre es: " + nombre_jugador + '\n')
print("Los jugadores que hay hasta ahora son: " + str(lista_jugadores) + '\n')
print("Tu presupuesto es de " + str(presupuesto) + " euros\n")

# Menu de opciones para agregar jugadores, eliminar jugadores, cambiar presupuesto y mostrar lo que ha introducido hasta ahora


print("Menu para introducir las opciones de cada jugador:\n")
while True:
	print("Escribe 'Otro jugador' si quieres agregar a otro jugador")
	print("Escribe 'Eliminar' si quieres eliminar algun jugador")
	print("Escribe 'Cambiar presupuesto' si quieres cambiar algun presupuesto")
	print("Escribe 'Agregar presupuesto' si quieres agregar el presupuesto de otro jugador")
	print("Escribe 'Historial' si quieres saber lo que has introducido hasta ahora")
	print("Escribe 'Continuar' si has terminado de configurar las opciones\n")


	input_usuario=input("Escriba su eleccion: ")

	if input_usuario.lower() == "otro jugador":               # Condicion para agregar otros jugadores
		agrega_jugador=input("Quieres agregar un jugador? Escribe si o no: ")
		if agrega_jugador.lower() == "si":
			jugador_nuevo=input("Escriba otro nombre, por favor: \n")
			lista_jugadores.append(jugador_nuevo)
		else:
			print("No se agrega ningun jugador mas")
		print("Los jugadores que hay hasta ahora son: " + str(lista_jugadores) + '\n')

	elif input_usuario.lower() == "eliminar":       # Condicion para eliminar jugadores
		elimina_jugador=str(input("Quieres eliminar algun jugador? Escribe si o no: "))
		if elimina_jugador.lower() == "si":
			eliminar=input("Que jugador quieres eliminar? : ")
			if eliminar in lista_jugadores:
				lista_jugadores.remove(eliminar)
			else:
				print("Ese jugador no se encuentra agregado")
		else:
			print("No se elimina ningun jugador \n")
		print("Los jugadores que hay hasta ahora son: " + str(lista_jugadores) + '\n')

	elif input_usuario.lower() == "agregar presupuesto": # Condicion para agregar el presupuesto de otros jugadores
		jugador = input("De que jugador quieres agregar un presupuesto? : ")
		if jugador in lista_jugadores:
			cantidad = float(input("Por favor, introduce un presupuesto con un maximo de 15 euros: "))
			while cantidad <= 0 or cantidad > 15:
				print("Presupuesto equivocado, vuelve a intentarlo")
				cantidad = float(input("Por favor, introduce un presupuesto con un maximo de 15 euros: "))
				break;
			else:
				lista_presupuesto.append(cantidad)
				print("El presupuesto de " + str(jugador) + " es de " + str(cantidad) + " euros\n")
		else:
			print("Ese jugador no se encuentra agregado\n")

	elif input_usuario.lower() == "cambiar presupuesto":    # Condicion para cambiar el presupuesto de cualquier jugador
		jugador_presupuesto = input("De que jugador quieres cambiar el presupuesto? : ")
		if jugador_presupuesto in lista_jugadores:
			try:
				presupuesto_nuevo = float(input("Por favor, introduce un nuevo presupuesto con un maximo de 15 euros: "))
				while presupuesto_nuevo <= 0 or presupuesto_nuevo > 15:
					print("Presupuesto equivocado, vuelve a intentarlo")
					presupuesto_nuevo = float(input("Por favor, introduce un presupuesto con un maximo de 15 euros: \n"))
				else:
					print("Tu nuevo presupuesto es de " + str(presupuesto_nuevo) + " euros\n")
					lista_presupuesto.append(presupuesto_nuevo)
					lista_presupuesto.remove(presupuesto or cantidad)
			except NameError:
				print("No se permiten letras, vuelve a intentarlo")
		else:
			print("Ese jugador no se encuentra en la lista")

	elif input_usuario.lower() == "historial":     # Condicion para ver los datos introducidos hasta ahora
		print("Los jugadores que hay hasta ahora son: " + str(lista_jugadores) + '\n')
		print("Los presupuestos que hay hasta ahora son, en orden:  " + str(lista_presupuesto) + '\n')
		if lista_jugadores == []:
			nombre_jugador=str(input("Escribe tu nombre: \n"))
			lista_jugadores.append(nombre_jugador)
		elif len(lista_jugadores) != len(lista_presupuesto):
			print("Falta por agregar el presupuesto de algun jugador\n")

	elif input_usuario.lower() == "continuar":     # Condicion para salir del bucle y seguir con el programa
		if lista_jugadores == []:
			print("Tienes que introducir antes tu nombre")
			nombre_jugador=str(input("Escribe tu nombre: \n"))
			lista_jugadores.append(nombre_jugador)
		elif len(lista_jugadores) != len(lista_presupuesto):
			print("Falta por agregar el presupuesto de algun jugador\n")
		break;
    
	else:                                         # Condicion por si escribe otra cosa desconocida
		print("Valor desconocido, vuelve a intentarlo \n")

#lista_jugadores=[]
#lista_jugadores.append(nombre_jugador)


#key=nombre_jugador
#value=presupuesto

#recopilacion_jugador={key:value}
#print(recopilacion_jugador)


print(lista_presupuesto[:])
print(lista_jugadores[:])

# Para hacer el sorteo de forma aleatoria

#print("A continuacion se barajaran los jugadores de forma aleatoria")
#random.choice(recopilacion_jugador) ???

# Guardar en archivo externo

#archivo_externo=open("AmigoInvisible.txt","w")
#frase=recopilacion_jugador
#archivo_externo.write(str(frase))
#archivo_externo.close()



"""
lista.jugadores2=[]

if input_usuario.lower() == "agregar":
	nombre_jugador=str(input("Escribe tu nombre: \n"))
	lista_jugadores.append(nombre_jugador)
	print("Tu nombre es: " + nombre_jugador + '\n')
	pregunta=input("Quieres agregar algun otro jugador? Escribe si o no \n")
	if pregunta.lower() == "si":
		jugador_nuevo=input("Escriba otro nombre, por favor: \n")
		lista_jugadores2.append(jugador_nuevo)
	else:
		print("No se agrega ningun jugador mas")
	print("Los jugadores que hay hasta ahora son: " + str(lista_jugadores) + '\n')
"""