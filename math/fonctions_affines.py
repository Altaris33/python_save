# Fonction affine défini une courbe linéaire avec une pente (coefficient directeur a) et une coordonnée à l'origine (b)

def function_affine(direct_coef_a,x1,x2,y1,y2,origin_coord_b):
    x1 = float(input('Enter x1 : '))
    x2 = float(input('Enter x2 : '))
    y1 = float(input('Enter y1 : '))
    y2 = float(input('Enter y2 : '))

    direct_coef_a = (y2 - y1)/(x2 - x1)
    origin_coord_b = y1 - direct_coef_a * x1

    print (f'The direct coefficient is : {direct_coef_a} and the origin coord is {origin_coord_b} !')
    print('\n')
    