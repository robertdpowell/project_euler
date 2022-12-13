import math
import networkx as nx

with open("input.py") as f:
    ls = [x.strip().split(' ') for x in f.read().strip().split("\n")]
    print (ls)


    num_of_rows = len(ls)
    num_of_cols = len(ls[0])

    max_product = 0


    for row in range (0, num_of_rows):
        for col in range(0, num_of_cols):
            # right prods
            maxright_product = sum(math.prod(range([row][x], [row][x]+4)))
            if (maxright_product > max_product)for x in range(col):
                max_product = maxright_product


