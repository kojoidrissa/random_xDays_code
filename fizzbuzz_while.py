# #attempting the Fizzbuzz problem with a While loop

i = 1
while i <= 100:
    if i % (3*5) == 0:
        print (i, "FizzBuzz")
    elif i % 5 == 0:
        print(i, "Buzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    else:
        print (i)
    i +=1


