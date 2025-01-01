from graphics.circle import *
from graphics.rectangle import *
from graphics.threedGraphics import cuboid,sphere

r=int(input("Enter the radius of Circle:\t"))
print(f"The area is {circArea(r):.2f} and Circumference is {circPeri(r):.2f}")

l,b=map(int,(input("Enter the length & breadth of Rectangle:\t").split()))
print(f"The area is {rectArea(l,b):.2f} and Perimeter is {rectPeri(l,b):.2f}")

l,h,w=map(int,input("Enter the length,height,width of Cuboid:\t").split())
print(f"The area is{cuboid.cuboidArea(l,h,w):.2f} and Volume is {cuboid.cuboidVol(l,h,w):.2f}")

r=int(input("Enter the radius of Sphere:\t"))
print(f"The area is {sphere.sphereArea(r):.2f} and Circumference is {sphere.sphereVol(r):.2f}")