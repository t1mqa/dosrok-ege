import re
import string

with open('24task.txt', 'r+') as taskFile:
    line = taskFile.readline()
    double = line
    line = line.replace('X', '0')
    line = line.replace('Y', '0')
    line = line.replace('Z', '0')
    for x in string.ascii_uppercase:
        line = line.replace(x, '1')
    line = line.replace('00', '2')
    data = re.findall('2[^2]*2', line)
    data = [len(x) for x in data]
    print(max(data))
