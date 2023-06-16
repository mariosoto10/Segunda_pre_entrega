from modulo1 import Cliente

opcion = str(input("Bienvenido a nuestra tienda. Para un mejor servicio, por favor elige tu preferencia: \n\n a. Fútbol. \n b. Hockey. \n c. Basket. \n d. Otros.\n"))

class Futbolero(Cliente):

    def __init__(self, hincha, nombre, email, edad, interes, hobbie):
        Cliente.__init__(self, nombre, email, edad, interes, hobbie)
        self.hincha = hincha

    def comprar(self):
        print('El cliente compró una camiseta de su equipo', self.hincha)

    def __str__(self):
        return f'Al cliente {self.nombre} de {self.edad} años le interesa el fútbol, le gusta el equipo {self.hincha} y su hobbie es {self.hobbie}'


class Hockey(Cliente):

    def __init__(self, hincha, nombre, email, edad, interes, hobbie):
        Cliente.__init__(self, nombre, email, edad, interes, hobbie)
        self.hincha = hincha

    def comprar(self):
        print('El cliente compró una camiseta de su equipo', self.hincha)

    def __str__(self):
        return f'Al cliente {self.nombre} de {self.edad} años le interesa el hockey, le gusta el equipo {self.hincha} y su hobbie es {self.hobbie}'


class Basket(Cliente):

    def __init__(self, hincha, nombre, email, edad, interes, hobbie):
        Cliente.__init__(self, nombre, email, edad, interes, hobbie)
        self.hincha = hincha

    def comprar(self):
        print('El cliente compró una camiseta de su equipo', self.hincha)

    def __str__(self):
        return f'Al cliente {self.nombre} de {self.edad} años le interesa el basket, le gusta el equipo {self.hincha} y su hobbie es {self.hobbie}'


class Otros(Cliente):

    def __init__(self, hincha, nombre, email, edad, interes, hobbie):
        Cliente.__init__(self, nombre, email, edad, interes, hobbie)
        self.hincha = hincha

    def comprar(self):
        print('El cliente le gusta un deporte extraño y compró una camiseta de su equipo', self.hincha)

    def __str__(self):
        return f'Al cliente le interesa un deporte extraño.'

hincha1 = str(input("¿De qué equipo eres hincha?"))
nombre1 = str(input("Escribe tu nombre."))
email1 = str(input("Escribe tu email."))
edad1 = int(input("Escribe tu edad."))
interes1 = str(input("Escribe tu interés."))
hobbie1 = str(input("Escribe tu hobbie."))

if opcion == "a" or opcion == "a.":

    cliente1 = Futbolero(hincha1, nombre1, email1, edad1, interes1, hobbie1)
    cliente1.comprar()
    cliente1.preguntar()
    print(cliente1)

elif opcion == "b" or opcion == "b.":
    
    cliente1 = Hockey(hincha1, nombre1, email1, edad1, interes1, hobbie1)
    cliente1.comprar()
    cliente1.preguntar()
    print(cliente1)

elif opcion == "c" or opcion == "c.":
    
    cliente1 = Basket(hincha1, nombre1, email1, edad1, interes1, hobbie1)
    cliente1.comprar()
    cliente1.preguntar()
    print(cliente1)

else: 

    cliente1 = Otros(hincha1, nombre1, email1, edad1, interes1, hobbie1)
    cliente1.comprar()
    cliente1.preguntar()
    print(cliente1)