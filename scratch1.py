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
even = lambda n:n % 2 == 0
print(even(4))
print(even(5))
data = [(1,'banana'), (2,'apple'), (3,'cherry')]
data.sort(key=lambda x: x[1])
print(data) # [(2, 'apple'), (1, 'banana'), (3, 'cherry')]
def square(n):
    return n * n
get_square = lambda x:square(x)
print(get_square(5))
celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)
words = ["Apple", "banana", "Cat", "dog", "Elephant"]
result = list(filter(lambda word: word[0].isupper(), words))
print(result)
from functools import reduce
nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, nums)
print(result)
people = [("Ravi", 25), ("Priya", 20), ("Amit", 30)]
result = sorted(people, key=lambda x: x[1], reverse=True)
print(result)
nums = [1,2,3,4,5,6,7,8,9,10]
result = list(map(lambda x: x*x,filter(lambda x: x % 2 == 0, nums)))
print(result)
def my_map(func, lst):
    result = []
    for item in lst:
        result.append(func(item))
    return result
nums = [1, 2, 3, 4]
print(my_map(lambda x: x * 2, nums))
print(list(map(lambda x: x * 2, nums)))
from functools import reduce
words = ['cat', 'elephant', 'dog', 'rhinoceros']
result = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(result)