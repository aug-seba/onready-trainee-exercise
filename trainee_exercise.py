class Vehiculo(object):
	
	def __init__(self,marca,modelo,precio):
		self.marca = marca
		self.modelo = modelo
		self.precio = precio
		
	def get_marca(self):
		return self.marca
	
	def get_modelo(self):
		return self.modelo
	
	def get_precio(self):
		return self.precio
		
	def __str__(self):
		return f'Marca:{self.marca}//Modelo:{self.modelo}// Precio:${self.precio:.2f}'

class Auto(Vehiculo):
	
	def __init__(self,marca,modelo,precio,puertas):
		super().__init__(marca,modelo,precio)
		self.puertas = puertas
		
	def __str__(self):
		return super().__str__().replace(" ",f'Puertas:{self.puertas}//')
		
	
class Moto(Vehiculo):

	def __init__(self,marca,modelo,precio,cilindradas):
		super().__init__(marca,modelo,precio)
		self.cilindradas = cilindradas
		
	def __str__(self):
		return super().__str__().replace(" ",f'Cilindradas:{self.cilindradas}//')

class DepositoVehiculos():
    def __init__(self,autos):
        self.autos = autos
    
    def max_precio(self):
        m = max([(m.precio,m.marca,m.modelo) for m in self.autos])
        return m
    
    def min_precio(self):
        mi = min([(m.precio,m.marca,m.modelo) for m in self.autos])
        return mi
    
    def contains_y(self):
        m = [(m.marca,m.modelo,m.precio) for m in self.autos if 'Y' in m.getModelo()]
        return m
    
lista_vehiculos = []
lista_vehiculos.append(Auto('Peugeot','206',puertas =4,precio=200000))
lista_vehiculos.append(Moto("Honda","Titan",cilindradas="125cc",precio = 60000))
lista_vehiculos.append(Auto("Peugeot",'208',puertas=5,precio = 250000))
lista_vehiculos.append(Moto("Yamaha","YBR",cilindradas="160cc",precio=80500.5))

t = DepositoVehiculos(lista_vehiculos)

for ve in t.autos:
    print(ve)

print('='*20)

print(f"Vehiculo mas caro: {t.max_precio()[1]} {t.max_precio()[2]}")
print(f"Vehiculo mas barato: {t.min_precio()[1]} {t.min_precio()[2]}")
print('='*20)

print(f"Vehiculo que contiene en el modelo la letra Y: {t.contains_y()[0][0]} {t.contains_y()[0][1]} ${t.contains_y()[0][2]:.2f}")

ord_list_veh = sorted(lista_vehiculos,key=lambda x:x.precio,reverse=True)

print('='*20)
print("Vehiculo ordenados de mayor a menor por precio: ")
for v in ord_list_veh:
    print(v)


