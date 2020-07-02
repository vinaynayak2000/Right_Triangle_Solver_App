#imports math module
import math

print("Welcome to the Right Triangle Solver App")
#Takes the input and converts into float 
side_a = float(input("What is the first leg of the triangle: "))
side_b = float(input("What is the second leg of the triangle: "))
#Calculates hypotenuse and area
hyp = math.sqrt(side_a**2 + side_b**2)
area =0.5 * side_a * side_b
#rounds upto 3 decimal places
hyp = round(hyp,3)
area = round(area,3)
#prints the output
print("For a triangle with legs of "+str(side_a)+" and "+str(side_b)+" the hypotenuse is "+str(hyp)+".")
print("For a triangle with legs of "+str(side_a)+" and "+str(side_b)+" the area is "+str(area)+".")

