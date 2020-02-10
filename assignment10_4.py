fname = input('Enter the file name:')
fhandle = open(fname)

counts = dict()
res=list()
time=list()
for line in fhandle:
    if line.startswith('From'):
        res = line.split()
        if not res[0] == 'From:':
            time = res[5].split(':')
            counts[time[0]] = counts.get(time[0],0) + 1

for k,v in sorted(counts.items()):
    print(k,v)
