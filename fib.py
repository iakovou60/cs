def fib(n):
    num1, num2 = 0, 1
    for _ in range(n):
        yield num1
        num1, num2 = num2, num1 + num2


print(list(fib(5)))

def test_fib():
    assert fib(5) == [0,1,1,2,3]