def apply_operation(a, b, op):
    return op(a, b)
print(apply_operation(10, 5, lambda x, y: x + y))
print(apply_operation(10, 5, lambda x, y: x - y))
print(apply_operation(10, 5, lambda x, y: x * y))
def recursive_sum(*args):
    if len(args) == 0:
        return 0
        if len(args) == 1:
        return args[0]
    return args[0] + recursive_sum(*args[1:])
print(recursive_sum(1, 2, 3, 4, 5))
def make_greeting(name, prefix="Hello", formatter=lambda x: x):
    greeting = prefix + " " + name
    return formatter(greeting)
print(make_greeting("Hema"))
print(make_greeting(name="Hema", formatter=str.upper))
nums = list(range(1, 21))
result = list(
    map(
        lambda x: x * x,
        filter(lambda x: x % 3 == 0, nums)
    )
)
print(result)
double = lambda x: x * 2
triple = lambda x: x * 3
quadruple = lambda x: x * 4
funcs = [double, triple, quadruple]
def apply_all(funcs, value):
    for f in funcs:
        value = f(value)
    return value
print(apply_all(funcs, 2))
def flatten(lst, depth=1):
    result = []
    for item in lst:
        if isinstance(item, list) and depth > 0:
            result.extend(flatten(item, depth - 1))
        else:
            result.append(item)
    return result
print(flatten([[1,[2]],3], depth=2))
from functools import reduce
def weighted_average(**scores):
    values = list(scores.values())
    total = reduce(lambda x, y: x + y, values)
    return total / len(values)
print(weighted_average(Maths=80, English=70, Science=90))
students = [
    {"name": "Ravi", "score": 75},
    {"name": "Priya", "score": 50},
    {"name": "Amit", "score": 85}
]
passed = filter(lambda s: s["score"] >= 60, students)
graded = map(
    lambda s: {"name": s["name"], "score": s["score"], "grade": "Pass"},
    passed
)
result = sorted(graded, key=lambda x: x["score"], reverse=True)
print(result)
data = [
    ("Ravi", 75),
    ("Priya", 90),
    ("Amit", 60)
]
strategies = {
    "by_name": lambda x: x[0],
    "by_score": lambda x: x[1],
    "by_length": lambda x: len(x[0])
}
choice = "by_score"
result = sorted(data, key=strategies[choice])
print(result)
from functools import reduce

def calculator(*args, operation="add", **options):

    operations = {
        "add": lambda nums: reduce(lambda x, y: x + y, nums),
        "multiply": lambda nums: reduce(lambda x, y: x * y, nums),
        "max": lambda nums: max(nums),
        "min": lambda nums: min(nums)
    }

    if options.get("show_steps", False):
        print("Numbers:", args)
        print("Operation:", operation)

    result = operations[operation](args)
    if options.get("show_steps", False):
        print("Result:", result)
    return result
print(calculator(1, 2, 3, 4))
print(calculator(1, 2, 3, 4, operation="multiply"))
print(calculator(5, 10, 15, operation="max"))
print(calculator(1, 2, 3, 4, show_steps=True))