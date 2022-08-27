initBal = float(input('Enter outstanding balance: '))
annrate = float(input('Enter annual interest rate as decimal: '))
outbal = initBal
mir = annrate/12.0
monthlypaymentLB = outbal/12.0
monthlypaymentUB = outbal*(1+(annrate/12.0))**12.0/12.0

while True:
    outbal = initBal
    mmp = (monthlypaymentLB + monthlypaymentUB)/2
    print('monthly payment:', mmp)
    for months in range(1,13):
        outbal = outbal*(1+mir)-mmp
        print('balance: ', outbal)
        if outbal <= 0:
            break
    if outbal > 0:
        monthlypaymentLB = mmp
    if outbal < 0:
        monthlypaymentUB = mmp
    if (monthlypaymentUB-monthlypaymentLB) < 0.01:
        break
outbal = initBal
for months in range(1,13):
    outbal = outbal*(1+mir)-mmp
    if outbal <= 0:
        break

print(round(mmp,2))
print(months)
print(round(outbal,2))
