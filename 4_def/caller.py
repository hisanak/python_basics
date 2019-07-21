"""
simply import the FizzBuzz program and call the function start_fizzbuzz()
"""

import fizzbuzz as fb
print("imported fizzbuzz")

print("call start_fizzbuzz() from caller.py")
fb.start_fizzbuzz()


from fizzbuzz import start_fizzbuzz
print("call start_fizzbuzz() without fizzbuzz")
start_fizzbuzz()

