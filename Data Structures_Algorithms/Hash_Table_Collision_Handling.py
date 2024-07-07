# Hash Table Collision Handling

# Separate chaining or chaining is the approach used to separate keys trying to store their values in the same location

# Linked list is used for multiple keys to share same storage location

# Linear Probing is also used: This is done by finding available location where value could be stored

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):  # __getitem__ is a python standard operator for getting values
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):  # __setitem__ is a python standard operator for setting values
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))


    def __delitem__(self, key):  # __delitem__ is a python standard operator for deleting values
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

t = HashTable()
print(t.get_hash('march 6'), t.get_hash('march 17'))

t['march 6'] = 120
t['march 6'] = 78
t['march 8'] = 67
t['march 9'] = 4
t['march 17'] = 459

print(t.arr)
print(t["march 8"])

del t['[]']

print(t.arr)


# Hash Table Collision Handling

# Separate chaining or chaining is the approach used to handle collisions by using a list at each array index

class HashTable:
    def __init__(self):
        # Initialize the hash table with a fixed size of 10
        self.MAX = 10
        # Create an array of empty lists to handle collisions using chaining
        self.arr = [[] for i in range(self.MAX)]

    # Hash function to calculate the index for a given key
    def get_hash(self, key):
        hash = 0
        # Sum the ASCII values of all characters in the key
        for char in key:
            hash += ord(char)
        # Return the index within the array bounds
        return hash % self.MAX

    # Method to retrieve the value for a given key
    def __getitem__(self, key):
        h = self.get_hash(key)  # Get the hash index for the key
        # Iterate over the list at the hash index
        for element in self.arr[h]:
            if element[0] == key:  # If the key is found, return its value
                return element[1]

    # Method to insert or update a key-value pair
    def __setitem__(self, key, val):
        h = self.get_hash(key)  # Get the hash index for the key
        found = False
        # Iterate over the list at the hash index to check if the key already exists
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:  # If the key is found, update its value
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:  # If the key is not found, append the new key-value pair to the list
            self.arr[h].append((key, val))

    # Method to delete a key-value pair
    def __delitem__(self, key):
        h = self.get_hash(key)  # Get the hash index for the key
        # Iterate over the list at the hash index to find the key
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:  # If the key is found, delete it from the list
                del self.arr[h][index]

# Example usage of the hash table
t = HashTable()

# Print hash values for demonstration
print(t.get_hash('march 6'), t.get_hash('march 17'))

# Insert key-value pairs into the hash table
t['march 6'] = 120
t['march 6'] = 78  # Update value for the same key
t['march 8'] = 67
t['march 9'] = 4
t['march 17'] = 459

# Print the hash table array to see the stored key-value pairs
print(t.arr)

# Retrieve and print the value for the key 'march 8'
print(t["march 8"])

# Delete the key-value pair for 'march 6'
del t['march 6']

# Print the hash table array to see the remaining key-value pairs
print(t.arr)
