def solver(n):
    return ("Fizz Buzz" if not n % 5 else "Fizz") if not n % 3 else ("Buzz" if not n % 5 else str(n))


for t in range(1001):
    #print(t, solver(t))
    print('{{\n"input": "{0}",\n"answer": "{1}"\n}},\n'.format(t, solver(t)))