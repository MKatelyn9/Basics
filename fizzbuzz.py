numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , 14, 15, 16, 17, 18, 19, 20]
for i in numbers:
    if i % 3 == 0:
        if (i % 5 == 0):
            print("FizzBuzz")
        else:
            print("Fizz")
    elif  i % 5 == 0:
        print("Buzz")
    else:
        print(i)