"""
simple FizzBuzz program

say "Fizz" if the number is multiple of 3
say "Buzz" if the number is multiple of 5
say "FizzBuzz" if the number is multiple of 15(both 3 and 5)
say the number in other cases
"""


class GenericFizzBuzz:
    def __init__(self, fizz=3, buzz=5):
        assert isinstance(fizz, int)
        assert isinstance(buzz, int)
        self.fizz = fizz # set member variable
        self.buzz = buzz # from argument

    def reply(self, num):
        if num % self.fizz == 0 and num % self.buzz == 0:
            print("FizzBuzz")
        elif num % self.buzz == 0:
            print("Buzz")
        elif num % self.fizz == 0:
            print("Fizz")
        else:
            print(num)


if __name__ == "__main__":
    fizz_buzz = GenericFizzBuzz(5, 7)
    for i in range(30):
        fizz_buzz.reply(i)

