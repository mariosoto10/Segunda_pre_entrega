class Cliente:

    def __init__(self, nombre, email, edad, interes, hobbie):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.interes = interes
        self.hobbie = hobbie

    def __str__(self):
        return f"Nombre: {self.nombre}\n Email: {self.email}\n Edad: {self.edad}\n"
    
    def comprar(self):
        print(self.nombre, "Compró un artículo relacionado con", self.interes, "y", self.hobbie)

    def preguntar(self):
        print("Al cliente le interesa:", self.interes)

