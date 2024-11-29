class rectangle():
    def __init__(self, length,breadth):
        self.__length = length
        self.__breadth = breadth
        
    def perimeter(self):
        return 2*(self.__length + self.__breadth)
    
    def area(self):
        return self.__length * self.__breadth
    
rect1=rectangle(5,4)
rect2=rectangle(10,15)
print(f"Perimeter of First Retangle: {rect1.perimeter()}") 
print(f"Area of First Retangle: {rect1.area()}")
print(f"Perimeter of Second Retangle: {rect2.perimeter()}")
print(f"Area of First Retangle: {rect2.area()}")

if(rect1.area()>rect2.area()):
    print("rect1 is greater")
else:
    print("rect2 is greater")

    