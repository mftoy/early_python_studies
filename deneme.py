year = input("Enter Annual:")
annual = float(year)

year = input("Enter Years:")
yrs = float(year)

year = input("Enter Initial:")
cap = int(year)

year = input("Enter Percentage as %:")
dummy = float (year)
percent = 1 + dummy/100.00

#annual = 10000.00
#cap = 6000

for yr in range(yrs):
    cap = cap * percent
    cap = cap + annual

print('After', yrs, 'years, your total will be', cap)
last = input("Press enter to exit!")
