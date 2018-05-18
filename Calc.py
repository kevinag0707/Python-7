
def add(x, y):
   return x + y


def subtract(x, y):
   return x - y


def multiply(x, y):
   return x * y


def divide(x, y):
   return x / y


def remainder(x, y):
   return x % y


def power(x, y):
   return x ** y

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))


print("Select an operation.")
print("+")
print("-")
print("*")
print("/")
print("%")
print("**")

choice = input("Enter choice:")


if choice == '+':
   print(x,"+",y,"=", add(x,y))

elif choice == '-':
   print(x,"-",y,"=", subtract(x,y))

elif choice == '*':
   print(x,"*",y,"=", multiply(x,y))

elif choice == '/':
   print(x,"/",y,"=", divide(x,y))

elif choice == '%':
   print(x,"%",y,"=", remainder(x,y))

elif choice == '**':
   print(x,"**",y,"=", power(x,y))
else:
   print("Invalid operation")