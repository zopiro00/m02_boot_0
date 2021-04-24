class Polygon:
    def __init__(self, sides):
        self.sides = sides
    
    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")
        
    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter
    
class Triangle(Polygon):
    def display_info(self):
        print("A triangle has three sides")
        super().display_info()

class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral has four sides")

t1 = Triangle([5,6,7])
perimeter = t1.get_perimeter()
print("El perimetro es", perimeter)

t1.display_info()