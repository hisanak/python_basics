"""
simple FizzBuzz program

say "Fizz" if the number is multiple of 3
say "Buzz" if the number is multiple of 5
say "FizzBuzz" if the number is multiple of 15(both 3 and 5)
say the number in other cases
"""

def start_fizzbuzz():
    for i in range(8):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


if __name__ == "__main__":
    print("fizzbuzz.py is the main")
    start_fizzbuzz()

