# create a for loop using range from 2 to 10
for n in range(2, 10):
    # inside the loop, use another for loop from 2 to n
    for x in range(2, n):
        # test if n can be divided by integer x
        if n % x == 0:
            # if true, then display n and shows how n is divided
            print(n, 'equals', x, '*', n // x)
            # the break is to jump out from the second for loop
            break
    # when jumped out from the loop, if n can't be divided by an integer, the else statement will then be operated
    else:
        # the prime number will be displayed
        print(n, 'is a prime number')






