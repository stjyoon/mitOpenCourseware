initBal = float(input('Enter outstanding balance: '))
annrate = float(input('Enter annual interest rate as decimal: '))
outbal = initBal
mir = annrate/12.0
monthlypaymentLB = outbal/12.0
monthlypaymentUB = outbal*(1+(annrate/12.0))**12.0/12.0
months = 0

while round(monthlypaymentLB-monthlypaymentUB,2) != 0.00:
    months = 0
    mmp = (monthlypaymentLB + monthlypaymentUB)/2
    while outbal>0 and months < 12:
        outbal = outbal*(1+mir)-mmp
        months += 1
    if outbal < 0:
        monthlypaymentLB = mmp
    if outbal > 0:
        monthlypaymentUB = mmp

    if round(monthlypaymentLB-monthlypaymentUB,2) == 0.00:
        break

    outbal = initBal
print(mmp)
print(months)
print(outbal)
