# GENERATORS
# This is a simpler way of creating iterator because:
# No need to define iter() and next() methods
# No need to raise StopIteration exception

def remote_control_next():
    yield "CNN"
    yield "ESPN"


itr = remote_control_next()
print(itr)

print(next(itr))
print(next(itr))

for c in remote_control_next():
    print(c)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for f in fibonacci():
    if f > 50:
        break
    print(f)
