"""
simple FizzBuzz program

say "Fizz" if the number is multiple of 3
say "Buzz" if the number is multiple of 5
say "FizzBuzz" if the number is multiple of 15(both 3 and 5)
say the number in other cases
"""

for i in range(8):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        # say the number simply
        # str.format is usefull to print somethin in specific format
        print("Number: {0:2d}".format(i))

