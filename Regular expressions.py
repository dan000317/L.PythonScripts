import re

with open('regex_sum_1668026.txt','r') as f:
    data = f.read()
total = 0
count = 0
numbers = re.findall('[0-9]+',data)
for x in numbers:
    total += int(x)
    count += 1

print(total,count)