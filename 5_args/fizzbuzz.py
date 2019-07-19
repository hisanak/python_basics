"""
simple FizzBuzz program
show an example of how to write docstring
"""

# we can set default value with like num=15
def reply_fizzbuzz(num: int=15) -> str: # supported from python3.5
    """
    say "Fizz" if the number is multiple of 3
    say "Buzz" if the number is multiple of 5
    say "FizzBuzz" if the number is multiple of 15(both 3 and 5)
    say the number in other cases

    Parameters
    ----------
    num : int
        input value for FizzBuzz game

    Returns
    -------
    ret : str
        what to say

    TO SHOW THIS, PLEASE TYPE THE COMMAND `pydoc3 fizzbuzz.py`
    """
    assert isinstance(num, int)

    ret = ""

    if num % 3 == 0:
        ret += "Fizz"
    if num % 5 == 0:
        ret += "Buzz"
    if len(ret) == 0 or ret == "": # which one is okay, but i don't recommend ` ret is "" `
        ret += str(num) # (str + int) is illegal

    return ret


if __name__ == "__main__":
    print("fizzbuzz.py is the main")
    i = int(1)
    # i = float(1) # start_fizzbuzz() allows only int
    while i < 40:
        print(reply_fizzbuzz(i))
        i += 7 # i++ is illegal

    print("call reply_fizzubzz without any args")
    print(reply_fizzbuzz())

