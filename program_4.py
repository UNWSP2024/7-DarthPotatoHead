#Program Written By: Ainsley Bellamy
#Date Written: 03/06/2025
#Program Title: Distance_Calculator


# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.


#Math module to use the square root function.
import math
#Function to calculate the distance between the user's inputted coordinates. Pulls values from x1 and x2,
#which have multiple values.
def distance_calculator(x1,x2):
    x_difference = x1[0]-x2[0]
    y_difference = x1[1]-x2[1]
    z_difference = x1[2]-x2[2]
    coordinate_distance = math.sqrt(x_difference**2+y_difference**2+z_difference**2)
    return coordinate_distance

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)


def main():
#Empty lists to take user input and make it easier to convert to tuples.
    first_coordinates = []
    second_coordinates = []
#The loop uses this list to both iterate and change the variable letter with each iteration.
    axis = ["x","y","z"]
    for letter in axis:
        try:
            coordinate = float(input(f"Enter {letter}1 for coordinate 1: "))
#Append to appropriate list.
            first_coordinates.append(coordinate)
        except ValueError:
            print("Invalid input.")
            exit()
#Do the same thing for the second set of coordinates.
    for letter in axis:
        try:
            coordinate = float(input(f"Enter {letter}2 for coordinate 2: "))
            second_coordinates.append(coordinate)
        except ValueError:
            print("Invalid input.")
            exit()
#Convert lists of values to tuples.
    coordinate1_tuple = tuple(first_coordinates)
    coordinate2_tuple = tuple(second_coordinates)
#Pass these values into the distance_calculator() function.
    distance = distance_calculator(coordinate1_tuple, coordinate2_tuple)
    print(f"Here is the distance between coordinates {first_coordinates} and {second_coordinates}: {distance:.2f}")

if __name__ == "__main__":
    main()