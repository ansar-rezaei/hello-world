#function for calculating payment
def mounthly_payment(principal, annual_interest_rate, duration):
    n = duration * 12
    if annual_interest_rate == 0:
        r = principal/n
    else:
        r = (annual_interest_rate/100)/12
    m = (principal * ( r * pow((1+r) , n))) / (pow((1+r) , n) - 1)
    return m

#function for calculating remaining balance
def remainig_loan_balance(principal, annual_interest_rate, duration , number_of_payments):
    p = number_of_payments 
    n = duration * 12
    if annual_interest_rate == 0:
        r = principal*(1-p/n)
    else:
        r = (annual_interest_rate/100)/12
    rlb = (principal * ( pow((1+r) , n) - pow((1+r) , p))) / (pow((1+r) , n) - 1)
    return rlb

#main program
principal=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent):"))
duration=int(input("Enter loan duration in years: "))

print("LOAN AMOUNT:", int(principal), "INTEREST RATE (PERCENT):", int(annual_interest_rate))
print("DURATION (YEARS):", duration, "MONTHLY PAYMENT:", int(mounthly_payment(principal,annual_interest_rate,duration)))

print("YEAR: 1 BALANCE:", int(remainig_loan_balance(principal, annual_interest_rate, duration , 12)) ,"TOTAL PAYMENT", int(mounthly_payment(principal,annual_interest_rate,duration)*12))

print("YEAR: 2 BALANCE:", int(remainig_loan_balance(principal, annual_interest_rate, duration , 24)) ,"TOTAL PAYMENT", int(mounthly_payment(principal,annual_interest_rate,duration)*24))

print("YEAR: 3 BALANCE:", int(remainig_loan_balance(principal, annual_interest_rate, duration , 36)) ,"TOTAL PAYMENT", int(mounthly_payment(principal,annual_interest_rate,duration)*36))

print("YEAR: 4 BALANCE:", int(remainig_loan_balance(principal, annual_interest_rate, duration , 48)) ,"TOTAL PAYMENT", int(mounthly_payment(principal,annual_interest_rate,duration)*48))

print("YEAR: 5 BALANCE:", int(remainig_loan_balance(principal, annual_interest_rate, duration , 60)) ,"TOTAL PAYMENT", int(mounthly_payment(principal,annual_interest_rate,duration)*60))