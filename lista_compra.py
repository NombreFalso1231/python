def menu():
	print("1. Mostrar todos los productos posibles para comprar")
	print("2. Agregar productos")
	print("3. Eliminar productos")
	print("4. Historial")
	print("5. Sumar todo y finalizar\n")

def productos():
	print("Los productos que hay disponibles son: \n" + str(productos_totales.keys()) + '\n')

def agregar():
	producto = input("Que producto quieres agregar? \n")
	if producto.lower() not in productos_totales.keys():
		print("Ese producto no esta en los productos disponibles\n")
	else:
		try:
			cantidad = float(input("Cuanta cantidad en kilos quieres de " + producto + "?:\n"))
			valor = productos_totales.get(producto)
			precio = valor * cantidad
			lista_compra[producto] = precio
			print("Lo que llevas hasta ahora de lista es: " + str(lista_compra) + '\n')
		except ValueError:
			print("Valor desconocido. Vuelve a intentarlo\n")

def eliminar():
	eliminar = input("Que producto quieres eliminar?\n")
	if eliminar not in lista_compra:
		print("Este producto no esta en la lista de la compra, no se puede eliminar\n")
		print("Lo que llevas hasta ahora de lista es: " + str(lista_compra) + '\n')
	else:
		del lista_compra[eliminar]
		print("La lista que queda es: " + str(lista_compra) + '\n')

def historial():
	print("La lista de la compra que hay hasta ahora es: " + str(lista_compra) + '\n')

def sumar():
	seguro = input("Estas seguro de que quieres terminar? S/n: ")
	if seguro.lower() == "s":
		suma = sum(lista_compra.values())
		print("La suma de toda la compra es de: " + str(suma) + " euros" '\n')
		print("Los productos que vas a comprar son " + str(lista_compra.keys()))
	else:
		print("No se termina todavia")

productos_totales = {
	"calabacin":1, "berenjena":1, "pepino":1, "brocoli":1.3, "zanahoria":1, "pimientos":1, "repollo":1, "coliflor":1, "cebollas":0.6, 
	"puerro":0.5, "tomates":1, "naranjas":1, "platanos":1.3, "manzanas":0.5, "peras":0.5, "melocotones":0.5, "paraguayos":0.5, 
	"ciruelas":0.5, "nectarina":0.5, "patatas":1, "espinacas":1, "acelgas":1, "ajos":1, "harina":0.45, "garbanzos":0.56, "lentejas":0.56, 
	"alubias":0.56, "tomate frito":1, "leche":0.86, "avena":0.9, "maizena":0.6, "soja":1.5, "gluten":2.6, "couscous":1.55, 
	"sal":0.19, "azucar":0.4, "cereales":0.9, "arroz":0.5, "galletas avena":1.3, "galletas":0.9, "macarrones":0.8, "espaguetis":0.8, 
	"sopa":0.6, "cafe":1.15, "cacao":1.3, "pan bimbo":0.95, "pan":0.33, "fritos":0.45, "pan de ajo":0.9, "aceite girasol":0.99, 
	"detergente":2.5, "suavizante": 1.7, "salfuman":1, "gel":1, "champu":1, "te":0.67, "champinyones":1.25, "panecitos":0.68, "lechuga":1,
	"coles":0.8, "pipos":1, "judias verdes":0.85, "aceituna negra":0.85
}

lista_compra = {}
print("\nBIENVENIDO A TU LISTA DE LA COMPRA FAVORITA\n")
menu()

while True:
	input_usuario = input("Escribe el numero de la opcion que quieras: ")
	if input_usuario == "1":
		productos()
		menu()
	elif input_usuario == "2":
		agregar()
		menu()
	elif input_usuario == "3":
		eliminar()
		menu()
	elif input_usuario == "4":
		historial()
		menu()
	elif input_usuario == "5":
		sumar()
		break;
	else:
		print("Valor desconocido. Vuelve a intentarlo")
