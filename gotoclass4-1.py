def mounthly_payment(principal, annual_interest_rate, duration):
    n = duration * 12
    if annual_interest_rate == 0:
        r = principal/n
    else:
        r = (annual_interest_rate/100)/12
    m = (principal * ( r * pow((1+r) , n))) / (pow((1+r) , n) - 1)
    return m

m = mounthly_payment(1000.0,4.5,5)
print("m=",m)
