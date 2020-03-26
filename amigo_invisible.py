import random
from io import *

# Dar la bienvenida e introducir el presupuesto acordado por los jugadores

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
			print("El presupuesto acordado por los jugadores es de " + str(presupuesto) + " euros\n")
			break;
	except NameError:
		print("No se permiten letras, vuelve a intentarlo\n")
	except ValueError:
		print("No se permiten letras, vuelve a intentarlo\n")

# Menu de opciones para agregar jugadores, eliminar jugadores, cambiar presupuesto y mostrar lo que ha introducido hasta ahora

print("Menu para introducir las opciones de cada jugador:\n")
while True:
	print("1. Agregar jugadores")
	print("2. Eliminar jugador")
	print("3. Cambiar presupuesto acordado")
	print("4. Historial")
	print("5. Continuar\n")

	input_usuario=input("Escriba el numero de su eleccion: ")

	if input_usuario == "1":                   # Condicion para agregar jugadores
		agrega_jugador=input("Quieres agregar un jugador? S/n: ")
		if agrega_jugador.lower() == "s":
			nombre_jugador=str(input("Escribe tu nombre: \n"))
			if nombre_jugador in lista_jugadores:
				print("Este jugador ya existe. Escribe otro nombre")
				nombre_jugador=str(input("Escribe otro nombre: \n"))
			else:
				lista_jugadores.append(nombre_jugador)
				print("Tu nombre es: " + nombre_jugador + '\n')
		else:
			print("No se agrega ningun jugador")
		print("Los jugadores que hay hasta ahora son: " + str(lista_jugadores) + '\n')
		print("El presupuesto es de " + str(presupuesto) + " euros\n")

	elif input_usuario == "2":                 # Condicion para eliminar jugadores
		elimina_jugador=str(input("Quieres eliminar algun jugador? S/n: "))
		if elimina_jugador.lower() == "s":
			eliminar=input("Que jugador quieres eliminar? : ")
			if eliminar in lista_jugadores:
				lista_jugadores.remove(eliminar)
			else:
				print("Ese jugador no se encuentra agregado")
		else:
			print("No se elimina ningun jugador \n")
		print("Los jugadores que hay hasta ahora son: " + str(lista_jugadores) + '\n')

	elif input_usuario == "3":                # Condicion para cambiar el presupuesto
		cambio = input("Quieres cambiar el presupuesto acordado? S/n: ")
		if cambio.lower() == "s":
			try:
				presupuesto_nuevo = float(input("Por favor, introduce un nuevo presupuesto con un maximo de 15 euros: "))
				while presupuesto_nuevo <= 0 or presupuesto_nuevo > 15:
					print("Presupuesto equivocado, vuelve a intentarlo")
					presupuesto_nuevo = float(input("Por favor, introduce un presupuesto con un maximo de 15 euros: \n"))
				else:
					print("El nuevo presupuesto es de " + str(presupuesto_nuevo) + " euros\n")
					lista_presupuesto.append(presupuesto_nuevo)
					lista_presupuesto.remove(presupuesto)
			except NameError:
				print("No se permiten letras, vuelve a intentarlo\n")
			except ValueError:
				print("No se permiten letras, vuelve a intentarlo\n")
		else:
			print("No se cambia el presupuesto")

	elif input_usuario == "4":               # Condicion para ver los datos introducidos hasta ahora
		print("Los jugadores que hay hasta ahora son: " + str(lista_jugadores) + '\n')
		print("El presupuesto acordado hasta ahora es de: " + str(lista_presupuesto) + " euros" '\n')
		if lista_jugadores == []:
			nombre_jugador = str(input("Escribe tu nombre: \n"))
			lista_jugadores.append(nombre_jugador)

	elif input_usuario == "5":               # Condicion para salir del bucle y seguir con el programa
		if lista_jugadores == []:
			print("Tienes que introducir antes tu nombre")
			nombre_jugador = str(input("Escribe tu nombre: \n"))
			lista_jugadores.append(nombre_jugador)
		else:
			break;
    
	else:                                    # Condicion por si escribe otra cosa desconocida
		print("Valor desconocido, vuelve a intentarlo \n")


print(lista_presupuesto[:])
print(lista_jugadores[:])


# Hacer el sorteo de forma aleatoria

print("A continuacion se sorteara los jugadores de forma aleatoria \n")

lista_dar = []
lista_recibir = []
for jugador in str(lista_jugadores):
	while lista_jugadores != []:
		a = random.choice(lista_jugadores)
		b = random.choice(lista_jugadores)
		if a != b:
			print(a + " le regala a " + b)
			lista_dar.append(a)
			lista_jugadores.remove(a)
			lista_recibir.append(b)
			lista_jugadores.remove(b)
	else:
		for jugador in lista_recibir:
			x = random.choice(lista_recibir)
			y = random.choice(lista_dar)
			if x != y:
				print(x + " le regala a " + y)
				lista_recibir.remove(x)
				lista_dar.remove(y)

# Guardar en archivo externo

archivo_externo=open("AmigoInvisible.txt","w")
jug = lista_jugadores
pres = lista_presupuesto
archivo_externo.write(str(jug))
archivo_externo.write(str(pres))
archivo_externo.close()