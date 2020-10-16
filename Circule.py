#function to calculate Area and circumference of a rectangle

r = input("radius: ")

def rec_fun (r):
    r = abs(float(r))

    A = 3.14*(r**2)
    C = 2*3.14*r
    
    output_list = [A,C]
    return output_list

print(rec_fun(r))


