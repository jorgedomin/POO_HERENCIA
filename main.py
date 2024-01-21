class Panel:
    def __init__(self, Usuario):
        self.__id = Usuario

    def user(self, code):
        if code == 1111:
            self.__id = code
            print(f"Codigo correcto: {code}. Arrancando el programa: {self.__id}")
        else:
            print("Codigo incorrecto vuelve a intentarlo")


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_identificacion(self):
        return f"Vehículo de marca {self.marca}, modelo {self.modelo}"


class Coche(Vehiculo):
    def __init__(self, marca, modelo, numeroDePuertas, CasaComercial):
        super().__init__(marca, modelo)
        self.numeroDePuertas = numeroDePuertas
        self.CasaC = CasaComercial

    def mostrar_detalles(self):
        informacion_base = super().mostrar_identificacion()
        return f"{informacion_base}, con {self.numeroDePuertas}, puerta"


class Moto(Vehiculo):

    def __init__(self, marca, modelo, namee):
        super().__init__(marca, modelo)
        self.namee = namee

    def mostrar_resultado(self):
        data = super().mostrar_identificacion()
        return f"{data}, de {self.namee},propietario"


class Distribuidora:
    def Buscar(self):
        return "venta al por mayor y menor"


class Carros(Distribuidora):
    def Buscar(self):
        return "Buscando posibles clientes para compra y venta de carros"


class Motocicletas(Distribuidora):
    def Buscar(self):
        return "Buscando posibles clientes para compra y venta de Motocicletas"


# Creando objetos de las clases derivadas
mi_telefono = Carros()
mi_computadora = Motocicletas()

# Utilizando el método sobrescrito
print(mi_telefono.Buscar())
print(mi_computadora.Buscar())

mi_vehiculo = Vehiculo("Toyota", "Corolla")
print(mi_vehiculo.mostrar_identificacion())
# Creando un objeto de la clase Coche
mi_coche = Coche("Honda", "Civic", 4, "SucuMotor")
print(mi_coche.mostrar_detalles())

mi_moto = Moto("Quinqui", "Ez", "Jorge Dominguez")
print(mi_moto.mostrar_resultado())