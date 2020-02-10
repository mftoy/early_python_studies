fname = input('Enter the file name:')
fhandle = open(fname)

counts = dict()
for line in fhandle:
    if line.startswith('From'):
        res = line.split()
        if not res[0] == 'From:':
            counts[res[1]] = counts.get(res[1],0) + 1

bigaddress = None
bignumber = None
for address,number in counts.items():
    if bigaddress is None or number > bignumber:
        bigaddress = address
        bignumber = number

print(bigaddress,bignumber)
