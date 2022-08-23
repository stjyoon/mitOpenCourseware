print('enter balance')
bal = input()
bal = float(bal)

print('enter annual interest rate')
annrate = input()
annrate = float(annrate)

print('enter min monthly payment rate as decimal')
mmpr = input()
mmpr = float(mmpr)

total = 0

for i in range(12):
    mmp = mmpr * bal
    interestpaid = annrate / 12 * bal
    princ = mmp-interestpaid
    bal = bal-princ
    total += interestpaid + princ

    print('month' + str(i+1))
    print(round(mmp,2))
    print(round(princ,2))
    print(round(bal,2))

print('total paid:' + str((round(total,2))))
print('remaining' + str(round(bal,2)))
