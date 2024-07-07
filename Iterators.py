
# ITERATORS

array = ["hey", "bro", "you're", "awesome"]

for a in array:
    print(a)

print(dir(array))

itr = iter(array)
print(itr)

print(next(itr))
print(next(itr))
print(next(itr))

for key in {"one": 1, "two": 2}:
    print(key)
# Iterate from the back

itrt = reversed(array)
print(next(itrt))

# create remote control class

class RemoteControl:
    def __init__(self):
        self.channels = ["HBO", "CNN", "ABC", "ESPN", "LBC"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]


rmt = RemoteControl()
itrtr = iter(rmt)

print(next(itrtr))
print(next(itrtr))
print(next(itrtr))
print(next(itrtr))
print(next(itrtr))
print(next(itrtr))


arr = ["Banji", "James", "John", "Mark"]
print(next(iter(arr)))


