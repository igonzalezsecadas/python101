while True:
    try:
        limit = int(input("Input a positive Integer to FizzBuzz: "))
        if limit < 0:
            raise Exception("The integer has to be positive.")
        break
    except Exception as e:
        print(e)
        continue

for i in range(1, limit + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)