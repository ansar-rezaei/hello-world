#Print Prime Numbers between 1 to 50
n = 2

while (n<51):
    is_prime = True
    i=2
    while (i<n-1):
        if n%i==0:
            is_prime = False
            break
        i = i+1
    if (is_prime):
        print(n)
    n=n+1
    
    
