outbal = float(input('enter outstanding balance'))
annrate = float(input('enter annual interest rate as decimal'))
rembal = outbal

mir = annrate / 12.0
months = 0
mmp = 10
while outbal > 0:
    outbal = outbal * (1+mir) - mmp
    months += 1
    if months > 11:
        mmp += 10
        months = 0
        outbal = rembal
print(mmp)
print(months)
print(round(outbal,2))
