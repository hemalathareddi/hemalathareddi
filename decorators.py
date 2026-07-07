def validate_postive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg<0:
                print("Error: All arguments must be postive")
                return None
    return wrapper
@validate_postive
def multiply(a,b):
    return a+b
print(multiply(4,5))
print(multiply(2,5))
