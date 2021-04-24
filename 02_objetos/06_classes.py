class Perro():
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def __str__(self):
        return "Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
        
    def ladrad(self):
        if self.peso >= 8:
            print("Guau, guau")
        else:
            print("guf, guf")
        
cuqui = Perro("cuqui",3,12)
cuqui.ladrad()

canica = Perro("Canina", 8, 5)
canica.ladrad()