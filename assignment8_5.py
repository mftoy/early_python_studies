fname = input('Enter a file name:')
fh  = open(fname)
count = 0
res = list()

for line in fh:
    if line.startswith('From'):
        res = line.split()
        if not res[0] == 'From:':
            print(res[1])
            count = count + 1

print('There were', count, 'lines in the file with From as the first word')
