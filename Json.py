# JSON
name = {
    'name': 'tom',
    'address': '1 reen street, NY',
    'phone': '2342342345'
}

# XML

XML = """
<name>tom</name>
<address>1 green street, NY</address>
<phone>2342342345</phone>
"""

book = {}

book['tom'] = {'name': 'tom',
               'address': '1 green street, NY',
               'phone': '2342342345'}

book['banji'] = {'name': 'banji',
                 'address': '1 white house road, Washington DC',
                 'phone': '+1 344 233'}

import json

js = json.dumps(book)
print(js)
 

with open("D://AI Engineering//Python\My_Projects//Project1//book.txt", "w") as f:
    f.write(js)

file = open("D://AI Engineering//Python//My_Projects//Project1//book.txt", "r")
txt = file.read()


import json

books = json.loads(txt)

print(books)

type(books)


print(books["banji"])

print(books["banji"]["phone"])

for person in books:
    print(person)

for person, value in books.items():
    print(person, value)

for person in books:
    print(books[person])
