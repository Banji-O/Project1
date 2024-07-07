# Hash Table
# This is to show how dictionary works internally
# ord function is used to find ASC value for character


def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100

print(get_hash('march 28'))


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(Key)
        self.arr[h] = None

t = HashTable()
t['march 6'] = 130
print(f"The t hash table: \n{t['march 6']}")
print(f"t array: {t.arr}")




