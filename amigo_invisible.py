import random
from io import *

# Dar la bienvenida, introducir presupuesto e indicar presupuesto

print("\nBIENVENIDO AL AMIGO INVISIBLE\n")
while True:
	try:
		presupuesto = float(input("Por favor, introduce un presupuesto con un maximo de 15 euros: "))
		while presupuesto <= 0 or presupuesto > 15:
			print("Presupuesto equivocado, vuelve a intentarlo")
			presupuesto = float(input("Por favor, introduce un presupuesto con un maximo de 15 euros: "))
			break;
		else:
			print("Tu presupuesto es de " + str(presupuesto) + " euros\n")
			break;
	except NameError:
		print("No se permiten letras, vuelve a intentarlo")

lista_presupuesto=[]
lista_presupuesto.append(presupuesto)

# Menu de opciones para agregar jugadores, eliminar jugadores, cambiar presupuesto y mostrar lo que ha introducido hasta ahora

lista_jugadores=[]

print("Menu para introducir las opciones de cada jugador:\n")
while True:
	print("Escribe 'Agregar' si quieres agregar un jugador nuevo")
	print("Escribe 'Eliminar' si quieres eliminar a un jugador")
	print("Escribe 'Presupuesto' si quieres cambiar tu presupuesto")
	print("Escribe 'Historial' si quieres saber lo que has introducido hasta ahora")
	print("Escribe 'Continuar' si has terminado de configurar las opciones\n")


	input_usuario=input("Escriba su eleccion: ")

	if input_usuario.lower() == "agregar":          # Condicion para aregar jugadores
		nombre_jugador=str(input("Escribe tu nombre: \n"))
		lista_jugadores.append(nombre_jugador)
		print("Tu nombre es: " + nombre_jugador + '\n')
		print("Los jugadores que hay hasta ahora son: " + str(lista_jugadores) + '\n')

	elif input_usuario.lower() == "presupuesto":    # Condicion para cambiar el presupuesto
		print("Tu presupuesto anterior era de " + str(presupuesto) + " euros\n")
		try:
			presupuesto_nuevo = float(input("Por favor, introduce un nuevo presupuesto con un maximo de 15 euros: "))
			while presupuesto_nuevo <= 0 or presupuesto > 15:
				print("Presupuesto equivocado, vuelve a intentarlo")
				presupuesto_nuevo = float(input("Por favor, introduce un presupuesto con un maximo de 15 euros: \n"))
			else:
				print("Tu nuevo presupuesto es de " + str(presupuesto_nuevo) + " euros\n")
				lista_presupuesto.append(presupuesto_nuevo)
				lista_presupuesto.remove(presupuesto)
		except NameError:
			print("No se permiten letras, vuelve a intentarlo")

	elif input_usuario.lower() == "eliminar":       # Condicion para eliminar jugadores
		elimina_jugador=str(input("Quieres eliminar algun jugador? Escribe si o no: "))
		if elimina_jugador.lower() == "si":
			eliminar=input("Que jugador quieres eliminar? : ")
			for eliminar in lista_jugadores:
				lista_jugadores.remove(eliminar)
		else:
			print("No se elimina ningun jugador \n")
		print("Los jugadores que hay hasta ahora son: " + str(lista_jugadores) + '\n')

	elif input_usuario.lower() == "historial":     # Condicion para ver los datos introducidos hasta ahora
		if lista_jugadores == []:
			nombre_jugador=str(input("Escribe tu nombre: \n"))
			lista_jugadores.append(nombre_jugador)
		print("Tu nombre es " + nombre_jugador)
		print("Tu presupuesto es de " + str(lista_presupuesto) + " euros \n")

	elif input_usuario.lower() == "continuar":     # Condicion para salir del bucle y seguir con el programa
		if lista_jugadores == []:
			print("Tienes que introducir antes tu nombre")
			nombre_jugador=str(input("Escribe tu nombre: \n"))
			lista_jugadores.append(nombre_jugador)
		break;
    
	else:                                         # Condicion por si escribe otra cosa desconocida
		print("Valor desconocido, vuelve a intentarlo \n")

lista_jugadores=[]
lista_jugadores.append(nombre_jugador)


key=nombre_jugador
value=lista_presupuesto

recopilacion_jugador={key:value}
print(recopilacion_jugador)


print(lista_presupuesto[:])
print(lista_jugadores[:])

# Para hacer el sorteo de forma aleatoria

#random.choice(recopilacion_jugador) ???

# Guardar en archivo externo

archivo_externo=open("AmigoInvisible.txt","w")
frase=recopilacion_jugador
archivo_externo.write(str(frase))
archivo_externo.close()



"""
if input_usuario.lower() == "agregar":
		nombre_jugador=str(input("Escribe tu nombre: \n"))
		lista_jugadores.append(nombre_jugador)
		print("Tu nombre es: " + nombre_jugador + '\n')
		pregunta=input("Quieres agregar algun otro jugador? Escribe si o no \n")
		if pregunta.lower() == "si":
			jugador_nuevo=input("Escriba otro nombre, por favor: \n")
			lista_jugadores.append(jugador_nuevo)
		else:
			print("No se agrega ningun jugador mas")
		print("Los jugadores que hay hasta ahora son: " + str(lista_jugadores) + '\n')
"""