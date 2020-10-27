def remainig_loan_balance(principal, annual_interest_rate, duration , number_of_payments):
    p = number_of_payments 
    n = duration * 12
    if annual_interest_rate == 0:
        r = principal*(1-p/n)
    else:
        r = (annual_interest_rate/100)/12
    rlb = (principal * ( pow((1+r) , n) - pow((1+r) , p))) / (pow((1+r) , n) - 1)
    return rlb

m = remainig_loan_balance(1000.0,4.5,5,12)
print(m)
