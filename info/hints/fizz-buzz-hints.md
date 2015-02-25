## I have no idea how to start solving this mission

To check various cases, use [if-else](http://docs.python.org/3/tutorial/controlflow.html#if-statements) statements.

```python
if condition:
    do_something()
else if another_condition:
    do_something2()
else:
    do_something3()
```

## I need some help to proceed with the mission

You can check if a number is divisible with
[the % operator](http://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-long-complex).
Just do `if X % n == 0:` then X is divisible by n.
That sid, it's more pythonic to write `if not X % n:`

## I am gone half way through. Need help!

If you need the string representation of a number, the use [string conversion](http://docs.python.org/3/tutorial/introduction.html#strings).
`str(53) == "53"`
```
## I am stuck. I need a small hint.
 
You should check divisibility from specific to general. For example, is it divisible by 15:

```python
if not number % 15:
    return "FizzBuzz"
else if not number % 5:
    ...
    ...
```

## I tried all I could. Nothing works. SOS

Don't forget - your function should return the result, not print it.
```python
def checkio(number):
    ...
    ...
    return str(number)
```
