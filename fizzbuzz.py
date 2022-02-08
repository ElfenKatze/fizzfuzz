for fizz in range(0, 100):
    if fizz% 15 == 0:
        print ("fizzbuzz")
    elif fizz% 3 == 0:
        print ("fizz")
    elif fizz% 5 == 0:
        print ("buzz")
    else:
        print (fizz)
