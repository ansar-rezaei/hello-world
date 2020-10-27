#Prime Numbers with For Loop
i = 2

for n in range (2,51):
    is_prime = True
    for i in range (2,n):
        if n%i==0:
            is_prime = False
            break
        i = i+1
    if (is_prime):
        print (n)
