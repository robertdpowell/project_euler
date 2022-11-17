
def sumsquares():
    squares = []
    for i in range (1, 101):
        square = (i * i)
        squares.append((square))
    return sum(squares)

def squaresums():
    sums = []
    for i in range (1, 101):
        sums.append(i)
    return (sum(sums) * sum(sums))

print (squaresums() - sumsquares())
