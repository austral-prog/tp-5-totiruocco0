
def max_of_two(x, y):
    if x>y:
        return x
    else:
        return y
       
def max_of_three(x, y, z):
    if x>y>z or x>z>y:
        return x 
    elif y>x>z or y>z>x:
        return y 
    else:
        return z
    


