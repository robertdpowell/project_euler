list = []
evens = []

def fib(number_of_terms):
    first = 0
    second = 1
    fibnum = 0
    list.append(first)
    list.append(second)

    while fibnum < number_of_terms:
        fibnum = first + second
        list.append(fibnum)
        first = second
        second = fibnum

    for i in list:
        if (i % 2 == 0):
            evens.append(i)

    print (sum(evens))

fib(4000000)