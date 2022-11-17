sums = []
for i in range (100, 999):
    for j in range (100, 999):
        sum = (i * j)
        if str(sum) == ''.join(reversed(str(sum))):
            sums.append(sum)
print (max(sums))