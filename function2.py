def send_email(to, subject, body):
    print("Email Sent")
send_email(to="abc@gmail.com", subject="Hello", body="Hi")
def book_ticket(name, source, destination, tickets):
    print(name)
book_ticket(name="Alice", source="Delhi", destination="Mumbai", tickets=2)
def power(base, exponent=2):
    return base ** exponent
print(power(3))
print(power(3, 3))
def connect(host, port=3306, protocol='TCP'):
    print(host, port, protocol)
connect("localhost")
connect("localhost", 8080)
connect("localhost", 8080, "UDP")
def discount_price(price, discount=10):
    return price - (price * discount / 100)

print(discount_price(1000))
print(discount_price(1000, 20))
def create_profile(username, email, age):
    print("Username:", username)
    print("Email:", email)
    print("Age:", age)
create_profile(username="hema", email="hema@gmail.com", age=22)

