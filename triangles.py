import math

#Function that calculates any triangle's area using Heron's formula
def getAreaofTriangle(sides):
    #Heron's formula requires to calculate the triangle's semi-perimeter(s)
    s = (sides[0] + sides[1] + sides[2]) / 2
    area = math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))
    print("The area of this triangle is {} square units". format(round(area, 3)))

#Function to get the type of triangle
def getTypeofTriangle(sides):
    #Check if it's a  triangle
    if sides[2] > (sides[0] + sides[1]):
        print("These segments cannot form a triangle")
    else:
        #Check if it's equilateral
        if sides[0] == sides[1] == sides[2]:
            print("Equilateral triangle")
        elif sides[0] == sides[1] or sides[1] == sides[2]:
            print("Isosceles triangle")
        else:
            print("Scalene triangle")
        getAreaofTriangle(sides)

#Get the sides of the triangle from the user
sides = []
count = 0

while count < 3:
    side = input("Enter a side of the triangle: ")
    try:
        side = int(side)
    except:
        print("Invalid input")
        continue
    sides.append(side)
    count += 1
sides.sort()
getTypeofTriangle(sides)