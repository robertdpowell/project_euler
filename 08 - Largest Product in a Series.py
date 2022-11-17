from numpy import prod
with open('input.py') as s:
    s = list(map(int,("".join(line.strip() for line in s))))
    res = [prod(s[i:i+13]) for i in range(len(s))]
    print (max(res))



