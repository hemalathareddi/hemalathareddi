def multiply_all(*args):
    product = 1
    for num in args:
        product *= num
    return product
print(multiply_all(2, 3, 4))
print(multiply_all(5))
print(multiply_all())
def display_tags(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_tags(title="Python", version=3.12, author="Guido")
def describe_person(name, *hobbies):
    print(f"Name: {name}")
    print(f"Hobbies: {hobbies}")
describe_person("Alice", "reading", "coding", "gaming")
def create_html_tag(tag, **attributes):
    attrs = ' '.join([f"{key}='{value}' "
    for key, value in attributes.items()])
    print(f"<{tag} {attrs}>")
create_html_tag('a', href='https://python.org', target='_blank')
def mixed(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
mixed(10, 20, 30, 40, 50, name="Rahul", role="DevOps")