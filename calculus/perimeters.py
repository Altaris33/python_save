# Calculus of perimeters -> perimeter is sometimes used instead of circumference. 

#imports  -> warning do not use from math import * as it might pollute the global namespace and return errors
import math


#Square
def calculate_square_perimeter():
    """ This functions renders the perimeter of squares"""
    print('Welcome, this is the Square perimeter calculator.')
    side = input('Enter a side length : ')
    # If the user does not input a number
        # Implement a custom message and raise a ValueError (use a try statement)
    try:
        if side.isdecimal():
            squarePerimeter = float(side) * 4
            print(f'The perimeter of the given square' 
                  f' is : {squarePerimeter}')
        else:
            print(f'Sorry, {side} is not a number. Please re-enter'
                  f' a valid value.')    
    except ValueError:
        print('Please enter a number, not a letter.')
    

#Testing Square Perimeter Function 
calculate_square_perimeter()

#Rectangle
def calculate_rectangle_perimeter():
    """This function renders the perimeter of rectangles"""
    print('Welcome, this is the Rectangle perimeter calculator.')
    rectangle_height = input('Enter a height : ')
    rectangle_width = input('Enter a width : ')

    try:
        if rectangle_height.isdecimal() and rectangle_width.isdecimal():
            rectangle_perimeter = (float(rectangle_height) +  float(rectangle_width)) * 2
            print(f'The perimeter of the given rectangle'
                  f' is : {rectangle_perimeter}')
        elif not rectangle_height.isdecimal():
            print(f'Sorry, you have provided a rectangle height of {rectangle_height} as'
                  f' a wrong formatted input.')
        elif not rectangle_width.isdecimal():
            print(f'Sorry, you have provided a rectangle width of {rectangle_width} as'
                  f' a wrong formatted input.')
        else:
            pass
    except ValueError:
        print('A value error has been raised. This is caused by an'
              ' invalid format input.')

# Testing Rectangle Perimeter Function
calculate_rectangle_perimeter() 

#Circle - 3 cases 
# If we know the radius -> perimeter (P) = 2*PI*R where PI is a constant (approx 3.14) and R is the radius.
# If we know the diameter -> perimeter (P) = PI * D where D is the diameter. 
# If we know the area/surface -> perimeter (P) = sqrt(4*PI*A) where A is the area. 
def calculate_circle_perimeter():

    """This function renders the perimeter of a circle given specific requirements"""
    print('Welcome, this is the Circle perimeter calculator.')
    user_choice = input('What data do you have? Choose between radius, diameter or area : ')

    if user_choice == 'radius' or user_choice.lower == 'radius':
        circle_radius = input('Provide the radius : ')

        try:
            if circle_radius.isdecimal():
                circle_perimeter = 2 * math.pi * float(circle_radius)
                print(f'The perimeter/circumference of the given circle'
                    f' is : {circle_perimeter}')
            else:
                print(f'Sorry, {circle_radius} is not a correct number.'
                    f' Please provide a number.')          
        except ValueError:
            print('A value error has been raised. This is caused by an'
                ' invalid input.')

    elif user_choice == 'diameter' or user_choice.lower == 'diameter':
        circle_diameter = input('Provide the circle diameter : ')

        try:
            if circle_diameter.isdecimal():
                circle_perimeter_diameter = math.pi * float(circle_diameter)
    elif user_choice == 'area' or user_choice.lower == 'area':

    else:
        print('Please give us one of the three choices.')                    

# Testing Circle Perimeter Function
calculate_circle_perimeter()

# Cylinder 
    # Definition : a solid figure with 2 parallel circles of the same size at the top and bottom. 
    # The top and bottom of a cylinder are called the bases (B). The height (h) is the distance between these bases and is 
    # perpendicular to it. Each base is a circle that has a radius (r).
    # EXAMPLE => a can of soda

    # Surface and volume of a cylinder 
        # Volume of a cylinder => B*h (we need to find B)
        # Area of the base B => pi*r**2

        # Surface area :
            # To understand the formula for the surface area of a cylinder, think of a can of vegetables. 
            # It has three surfaces: the top, the bottom, and the piece that forms the sides of the can. 
            # If you carefully cut the label off the side of the can and unroll it, you will see that it is a rectangle. 
            # See the image below.
            # By cutting and unrolling the label of a can of vegetables, we can see that the surface of a cylinder is a rectangle. 
            # The length of the rectangle is the circumference of the cylinder’s base, and the width is the height of the cylinder.
def calculate_cylinder_volume(cylinder_height,base_radius):

    print("This is the cylinder volume and surface calculator !")

    cylinder_height = input('Provide a height : ') 
    base_radius = input('Provide a radius : ')

    try:
        if cylinder_height.isdecimal() and base_radius.isdecimal():
            cylinder_volume = float(math.pi*base_radius**2) * float(cylinder_height)
            print(f'The volume of the cylinder is : {cylinder_volume}.')
        else:
            print(f'Sorry, we coud not manage to find out the cylinder volume. Try again.')    
    except ValueError:
        print('Height or radius are not valid in format.')

def calculate_cylinder_surface_area(cylinder_height,base_radius,base):
    """This function will go further and calculate the surface area of a cylinder.
    A surface area is the area of the 2 circles (bases top and bottom) + the area of the unrolled rectangle (see description above)"""
    print("This is the cylinder surface area calculator !")      

    cylinder_height = input('Provide a height : ')
    base_radius = input('Provide a radius : ')
    base = float(math.pi * base_radius**2)

    try:
        if cylinder_height.isdecimal() and base_radius.isdecimal() and base.isdecimal():
            cylinder_volume = float(base) * float(cylinder_height)
            cylinder_surface = 2 * float(base) + 2 * (math.pi * float(base_radius) * float(cylinder_height)) 
            print(f'The global surface of the given cylinder is : {cylinder_surface}')
        else:
            print(f'Sorry, we could not manage to find out the cylinder surface. Try again.')    

        except: ValueError:
            print('Height, radius or base inconsistent.')

calculate_cylinder_volume()
calculate_cylinder_surface_area()            
    

                      
            
                      
