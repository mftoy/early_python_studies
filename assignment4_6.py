def computepay(h,r):
  if h < 41 :
      total = h * r
      return total
  else:
      total = r * (h + (h-40)* 0.5)
      return total

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
print (computepay(h,r))
