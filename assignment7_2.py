# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0.0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    #print(line)
    index = line.find(' ')
    #print(index)
    num = line[index:]
    #print(num)
    num1 = num.strip()
    #print(num1)
    num2 = float(num1)
    #print(num2)
    total = total + num2
    count = count + 1

print('Average spam confidence:', total/count)
