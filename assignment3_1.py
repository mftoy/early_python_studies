hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h < 41 :
    total = h * r
    print(total)
else:
    total = r * (h + (h-40)* 0.5)
    print(total)
