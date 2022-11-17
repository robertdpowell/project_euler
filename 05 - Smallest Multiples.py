multiples = []
for number in range(0, 500000000, 20):
    if all(number % i == 0 for i in range (1,20)):
        multiples.append(number)
print (multiples)
