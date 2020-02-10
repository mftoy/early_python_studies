largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num_ = int(num)
    except:
        print('Invalid Input')
        continue
    if largest is None :
        largest = num_
    if largest < num_:
        largest = num_
    if smallest is None :
        smallest = num_
    if smallest > num_:
        smallest = num_

print("Maximum is", largest)
print("Minimum is", smallest)
