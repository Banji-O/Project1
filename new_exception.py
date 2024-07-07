
"""
Exceptions are errors detected at the
time of program execution
"""

x = input("Enter number1: ")
y = input("Enter number2: ")
try:
    z = int(x) / int(y)
except Exception as e:
    print("exception occurred: ", e)
    print("exception type: ", type(e).__name__) # This will print the name of the exception error
    z = None
print("The division is: ", z)


# STANDARD EXCEPTIONS, USER DEFINED EXCEPTIONS, FINALLY
x = input("Enter number1: ")
y = input("Enter number2: ")

try:
    raise MemoryError("memory error")
except MemoryError as e:
    print(e)

class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def print_exception(self):
        print(self.msg, "Accident occurred. Take detour")

try:
    raise Accident("crash between two cars.")
except Accident as e:
    e.print_exception()

# FINALLY

def process_file():
    try:
        f = open("D:\\AI Engineering\\Python\\My_Projects\\Project1\\book.txt")
        x = 1/0
    except FileNotFoundError as er:
        print("inside except")
    finally:
        print("cleaning up file")
        f.close()
        print("file closed")

print(process_file())
