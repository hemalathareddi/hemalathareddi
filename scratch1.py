def mixed(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

mixed(10, 20, 30, 40, 50, name="Rahul", role="DevOps")
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier
times3 = make_multiplier(3)
print(times3(10))
times5 = make_multiplier(5)
print(times5(4))
max_num = lambda x, y: x if x > y else y
print(max_num(10, 7))
even = lambda n: n % 2 == 0
print(even(4))
print(even(5))
data = [(1,'banana'), (2,'apple'), (3,'cherry')]
data.sort(key=lambda x: x[1])
print(data) # [(2, 'apple'), (1, 'banana'), (3, 'cherry')]
def square(n):
    return n * n
get_square = lambda x: square(x)
print(get_square(5)) # 25