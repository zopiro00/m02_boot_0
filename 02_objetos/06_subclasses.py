class Perro():
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def __str__(self):
        return "Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
        
    def ladrar(self):
        if self.peso >= 8:
            print("Guau, guau")
        else:
            print("guf, guf")
        
class PerroAsistencia(Perro):
    def __init__(self,nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False
    def __str__(self):
        return "Perro de asistencia de {}".format(self.amo)
    def pasear(self):
        print("Ayudo a mi dueño {} a pasear.".format(self.amo))
    def ladrar(self):
        if self.trabajando:
            print("shhhh, no puedo ladrar.")
        else:
            Perro.ladrar(self)
    def trabajando(self,valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor