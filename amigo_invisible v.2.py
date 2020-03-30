from random import shuffle
from io import *

lista_presupuesto=[]
lista_jugadores=[]

def presupuesto(lista_presupuesto):   # Poner el presupuesto acordado.
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

def menu():   # Mostrar por pantalla el menu con las diferentes opciones
	print("Menu para introducir las opciones de cada jugador:\n")
	print("1. Agregar jugadores")
	print("2. Eliminar jugador")
	print("3. Cambiar presupuesto acordado")
	print("4. Historial")
	print("5. Continuar\n")

def agregar(lista_jugadores):   # Agregar jugadores a lista_jugadores
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

def eliminar(lista_jugadores):   # Eliminar jugadores de lista_jugadores
	elimina_jugador=str(input("Quieres eliminar algun jugador? S/n: "))
	if elimina_jugador.lower() == "s":
		eliminar=input("Que jugador quieres eliminar? : ")
		if eliminar in lista_jugadores:
			lista_jugadores.remove(eliminar)
		else:
			print("Ese jugador no se encuentra agregado")
	else:
		print("No se elimina ningun jugador \n")

def cambio_presupuesto(lista_presupuesto):   # Cambiar el presupuesto previamente acordado
	cambio = input("Quieres cambiar el presupuesto acordado? S/n: ")
	try:
		if cambio.lower() == "s":
			presupuesto_nuevo = int(input("Por favor, introduce un nuevo presupuesto con un maximo de 15 euros: "))
			while presupuesto_nuevo <= 0 or presupuesto_nuevo > 15:
				print("Presupuesto equivocado, vuelve a intentarlo")
				presupuesto_nuevo = int(input("Por favor, introduce un presupuesto con un maximo de 15 euros: \n"))
			else:
				print("El nuevo presupuesto es de " + str(presupuesto_nuevo) + " euros\n")
				lista_presupuesto.pop()
				lista_presupuesto.append(presupuesto_nuevo)
		else:
			print("No se cambia el presupuesto")
	except NameError:
		print("No se permiten letras, vuelve a intentarlo\n")
	except ValueError:
		print("No se permiten letras, vuelve a intentarlo\n")

def historial():   # Mostrar todos los datos introducidos hasta el momento
	print("Los jugadores que hay hasta ahora son: " + str(lista_jugadores) + '\n')
	print("El presupuesto acordado hasta ahora es de: " + str(lista_presupuesto) + " euros" '\n')
	if lista_jugadores == []:
		nombre_jugador = str(input("Escribe tu nombre: \n"))
		lista_jugadores.append(nombre_jugador)

def continuar():   # Comprobar que haya nombres en la lista_jugadores y si es el caso, continuar con el programa
	if lista_jugadores == []:
		print("Tienes que introducir antes tu nombre")
		nombre_jugador = str(input("Escribe tu nombre: \n"))
		lista_jugadores.append(nombre_jugador)

print("\nBIENVENIDO AL AMIGO INVISIBLE\n")

presupuesto(lista_presupuesto)
menu()

while True:
	input_usuario=int(input("Escriba el numero de su eleccion: "))
	if input_usuario == 1:
		agregar(lista_jugadores)
		menu()
	elif input_usuario == 2:
		eliminar(lista_jugadores)
		menu()
	elif input_usuario == 3:
		cambio_presupuesto(lista_presupuesto)
		menu()
	elif input_usuario == 4:
		historial()
		menu()
	elif input_usuario == 5:
		continuar()
		break;
	else:
		print("La opcion no es valida")

# Hacer el sorteo de forma aleatoria

print("A continuacion se sorteara los jugadores de forma aleatoria \n")
shuffle(lista_jugadores)
amigo_invisible = {lista_jugadores[i - 1]:lista_jugadores[i] for i in range(len(lista_jugadores))}
for jugador in lista_jugadores:
	print("A {0} le ha tocado {1}\n".format(jugador,amigo_invisible[jugador]))

# Guardar en archivo externo

archivo_externo=open("AmigoInvisible.txt","w")
jug = lista_jugadores
pres = lista_presupuesto
archivo_externo.write(str(jug))
archivo_externo.write(str(pres))
archivo_externo.close()




################APARTE################

#lista_dar = []
#lista_recibir = []
#for jugador in str(lista_jugadores):
#	while lista_jugadores != []:
#		a = random.choice(lista_jugadores)
#		b = random.choice(lista_jugadores)
#		if a != b:
#			print(a + " le regala a " + b)
#			lista_dar.append(a)
#			lista_jugadores.remove(a)
#			lista_recibir.append(b)
#			lista_jugadores.remove(b)
#	else:
#		for jugador in lista_recibir:
#			x = random.choice(lista_recibir)
#			y = random.choice(lista_dar)
#			if x != y:
#				print(x + " le regala a " + y)
#				lista_recibir.remove(x)
#				lista_dar.remove(y)