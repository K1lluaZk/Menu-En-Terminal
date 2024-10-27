import time

while True:
    
   print("Hola, bienvenido al menu de ejercicios.")
   print("------------------------------------------")
   print("|Menu de ejercicios|")
   print("-----------------------")
   print("Cargando....")
   print("Espera...")
   time.sleep(2)

   print("""Ejercicios:
|Poo|
1- ejercicio 1
2- ejercicio 2
3- ejercicio 3
4- ejercicio 4
5- ejercicio 5
-----------------------
6- Salir del menu""")
   print("-----------------------")
   elegir_ejercicio = int(input("Elige el numero del ejercicio:"))

   print("Cargando...")
   time.sleep(2)

   if elegir_ejercicio == 1:
      print("""
class Persona:
    
    def __init__(self, nombre, apellidos, edad, casado, numeroDocumentoIdentidad, profesion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.casado = casado
        self.numeroDocumentoIdentidad = numeroDocumentoIdentidad
        self.profesion = profesion
        
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre
        
    def set_apellidos(self, apellidos):
        self.apellidos = apellidos
        
    def get_apellidos(self):
        return self.apellidos
        
    def set_edad(self, edad):
        self.edad = edad
    
    def get_edad(self):
        return self.edad
        
    def set_casado(self, casado):
        self.casado = casado
        
    def get_casado(self):
        return self.casado
        
    def set_numeroDocumentoIdentidad(self, numeroDocumentoIdentidad):
        self.numeroDocumentoIdentidad = numeroDocumentoIdentidad
    
    def get_numeroDocumentoIdentidad(self):
        return self.numeroDocumentoIdentidad
        
    def set_profesion(self, profesion):
        self.profesion = profesion
        
    def get_profesion(self):
        return self.profesion
    
    def trabajar(self):
        if self.profesion == "Maestra":
            print(f"{self.nombre} esta impartiendo clases")
        elif self.profesion == "Doctor":
            print(f"{self.nombre} esta atendiendo pacientes")
        elif self.profesion == "Ingeniero en sistemas":
            print(f"{self.nombre} esta analizando un codigo")
        elif self.profesion == "Ingeniero civil":
            print(f"{self.nombre} esta revisando unos planos")
        elif self.profesion == "Taxista":
            print(f"{self.nombre} esta llevando a un cliente a su destino")
        elif self.profesion == "Cocinero":
            print(f"{self.nombre} esta preparando el menu de un restaurante")
        elif self.profesion == "Psicologo":
            print(f"{self.nombre} esta aplicando terapia")
    
    def descansar(self):
        print(f"{self.nombre} esta descansando")
        
    def presentar_documento(self):
        print(f"este es el documento de identidad de {self.nombre} |{self.numeroDocumentoIdentidad}|")
        
persona1 = Persona("Natti", "Gutierrez", 27, True, "001-0023450",  "Maestra", )
persona2 = Persona("Benito", "Martinez", 29, False, "402-1010293",  "Ingeniero civil", )
persona3 = Persona("Emmanuel", "Gazmey", 25, True, "404-9394231",  "Ingeniero en sistemas", )
persona4 = Persona("Alejandro", "Paz", 24, False, "001-9993229",  "Cocinero", )
persona5 = Persona("Maicol", "Santos", 20, False, "239-9394023",  "Taxista", )
persona6 = Persona("Myke", "Torres", 27, True, "001-9035042",  "Psicologo", )
persona7 = Persona("Raul", "Ocasio", 21, False, "402-9284586",  "Doctor", )
persona8 = Persona("Jésus", "Nieves", 32, False, "405-1290845",  "Ingeniero en sistemas", )
persona9 = Persona("Carlos", "Morales", 33, False, "495-2930332",  "Cocinero", )
    
persona1.trabajar()
persona2.trabajar()
persona3.trabajar()
persona4.trabajar()    
persona5.trabajar()
persona6.trabajar()
persona7.trabajar()
persona8.trabajar()
persona9.trabajar()
    
persona1.presentar_documento()
persona1.descansar()
""")
   elif elegir_ejercicio == 2:
      print("""class Cuenta:
    def __init__(self, titular="Desconocido", saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def ingreso(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han ingresado {cantidad} a la cuenta de {self.titular}. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a ingresar debe ser positiva.")

    def reintegro(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad} de la cuenta de {self.titular}. Saldo actual: {self.saldo}")
        else:
            print("Cantidad no válida o saldo insuficiente.")

    def transferencia(self, otra_cuenta, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            otra_cuenta.saldo += cantidad
            print(f"Se han transferido {cantidad} de la cuenta de {self.titular} a la cuenta de {otra_cuenta.titular}.")
        else:
            print("Cantidad no válida o saldo insuficiente.")

    def mostrar(self):
        print(f"Titular: {self.titular}, Saldo: {self.saldo}")
        
    def ingresar(self, cantidad):
        self.ingreso(cantidad)
        

cuenta1 = Cuenta("Mario", 1000)
cuenta2 = Cuenta("Luis", 500)

cuenta1.mostrar()
cuenta1.ingreso(200)
cuenta1.reintegro(100)
cuenta1.transferencia(cuenta2, 150)

cuenta1.mostrar()
cuenta2.mostrar()

        """)
    
   elif elegir_ejercicio == 3:
      print("""
import match

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        divisor_comun = math.gcd(self.numerador, self.denominador)
        self.numerador //= divisor_comun
        self.denominador //= divisor_comun

    def sumar(self, otra):
        nuevo_numerador = self.numerador * otra.denominador + otra.numerador * self.denominador
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def restar(self, otra):
        nuevo_numerador = self.numerador * otra.denominador - otra.numerador * self.denominador
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def multiplicar(self, otra):
        nuevo_numerador = self.numerador * otra.numerador
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def dividir(self, otra):
        if otra.numerador == 0:
            raise ValueError("No se puede dividir por una fracción con numerador cero.")
        nuevo_numerador = self.numerador * otra.denominador
        nuevo_denominador = self.denominador * otra.numerador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def mostrar(self):
        
        return f"{self.numerador}/{self.denominador}"
        
fraccion1 = Fraccion(3, 4)
fraccion2 = Fraccion(2, 5)

suma = fraccion1.sumar(fraccion2)
resta = fraccion1.restar(fraccion2)
multiplicacion = fraccion1.multiplicar(fraccion2)
division = fraccion1.dividir(fraccion2)

print("Suma:", suma.mostrar())
print("Resta:", resta.mostrar())
print("Multiplicación:", multiplicacion.mostrar())
print("División:", division.mostrar())

""")

   elif elegir_ejercicio == 4:
      print("""
class Complejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def sumar(self, otro):
        real = self.real + otro.real
        imaginario = self.imaginario + otro.imaginario
        return Complejo(real, imaginario)

    def restar(self, otro):
        real = self.real - otro.real
        imaginario = self.imaginario - otro.imaginario
        return Complejo(real, imaginario)

    def multiplicar(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return Complejo(real, imaginario)

    def dividir(self, otro):
        if otro.real == 0 and otro.imaginario == 0:
            raise ValueError("No se puede dividir por un número complejo cero.")
        divisor = otro.real ** 2 + otro.imaginario ** 2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / divisor
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / divisor
        return Complejo(real, imaginario)

    def mostrar(self):
        signo = '+' if self.imaginario >= 0 else '-'
        return f"{self.real} {signo} {abs(self.imaginario)}i"
        
complejo1 = Complejo(3, 4)
complejo2 = Complejo(1, -2)

suma = complejo1.sumar(complejo2)
resta = complejo1.restar(complejo2)
multiplicacion = complejo1.multiplicar(complejo2)
division = complejo1.dividir(complejo2)

print("Suma:", suma.mostrar())
print("Resta:", resta.mostrar())
print("Multiplicación:", multiplicacion.mostrar())
print("División:", division.mostrar())

        
        """)
    
   elif elegir_ejercicio == 5:
      print("""
class Cliente:
    def __init__(self, nombre, cantidad=0):
        self.nombre = nombre
        self.cantidad = cantidad

    def depositar(self, monto):
        if monto > 0:
            self.cantidad += monto
            print(f"{self.nombre} ha depositado {monto}. Saldo actual: {self.cantidad}")
        else:
            print("El monto a depositar debe ser positivo.")

    def extraer(self, monto):
        if monto > 0 and monto <= self.cantidad:
            self.cantidad -= monto
            print(f"{self.nombre} ha extraído {monto}. Saldo actual: {self.cantidad}")
        else:
            print("Monto no válido o saldo insuficiente.")

    def mostrar_total(self):
        return f"{self.nombre} tiene un saldo de {self.cantidad}"


class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Mario")
        self.cliente2 = Cliente("Ana")
        self.cliente3 = Cliente("Luis")

    def operar(self):
        # Ejemplo de operaciones
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente1.extraer(50)
        self.cliente2.extraer(30)

    def deposito_total(self):
        total = self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad
        print("Total de dinero en el banco al final del día:", total)

    def mostrar_clientes(self):
        print(self.cliente1.mostrar_total())
        print(self.cliente2.mostrar_total())
        print(self.cliente3.mostrar_total())
        
 
banco = Banco()

banco.operar()

banco.mostrar_clientes()

banco.deposito_total()

        
""")
    
   elif elegir_ejercicio == 6:
      print("Saliendo del menu...")
      break 
   else:
      print("Ingresa un ejercicio valido")