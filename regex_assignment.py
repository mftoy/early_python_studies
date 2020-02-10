import re

fname = input('Enter the file name:')
fhandle = open(fname)

numbers = list()
for line in fhandle:
    y = re.findall('[0-9]+',line)
    if len(y) != 0 :
        #print(y)
        for i in y:
            numbers.append(int(i))
        #print(numbers)
        #print('Sum of this line is', str(sum(y)))
        #numbers = numbers + sum(y)
        #print('Total is', str(numbers) , 'right now!')

#print('The End!')
print(sum(numbers))
