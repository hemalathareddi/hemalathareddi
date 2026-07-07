import functools
def valid(func):
    @functools.wraps(func)
    def inner(a,b):
        if not isinstance(a,str):
            a=str(a)
        if not isinstance(b,str):
            b=str(b)
        return func(a,b)
    return inner

@valid
def fun(a:str,b:str) -> str:
    return a+b

print(fun.__name__)
print(fun("12","13"))
print(fun(25,30))
print(fun.__annotations__)
print(fun.__doc__)
print(print.__doc__)
