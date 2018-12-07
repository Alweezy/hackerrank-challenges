class HashMap:
    """blueprint for creating the hashmap
    """

    def __init__(self):
        self.size = 6
        self.hash_map = [None] * self.size

    def _get_hash(self, key):
        """The method to do the actual hashing
        """
        hash = 0
        for char in key:
            hash += ord(char)

        return hash % self.size

    def add_values(self, key, value):
        """Method to add values to the table
        """
        hash_value = self._get_hash(key)
        key_value = [key, value]

        if self.hash_map[hash_value]:
            for pair in self.hash_map[hash_value]:
                if pair[0] == key:
                    pair[1] = value
                    return True
        else:
            self.hash_map[hash_value] = list([key_value])
            return True

    def get_value(self, key):
        """method gets a value for a given key
        """
        hash_value = self._get_hash(key)

        if self.hash_map[hash_value]:
            for pair in self.hash_map[hash_value]:
                if pair[0] == key:
                    return pair[1]
        else:
            return None

    def delete_value(self, key):
        """Deletes a value based on a given key
        """
        hash_value = self._get_hash(key)

        if self.hash_map[hash_value]:
            for i in range(0, len(self.hash_map[hash_value])):
                if self.hash_map[hash_value][i][0] == key:
                    self.hash_map[hash_value].pop(i)
                    return True
        else:
            return None

    def print_all(self):
        """Prints all the entries into our hash table
        """
        for entry in self.hash_map:
            if entry:
                print(entry)


h = HashMap()

h.add_values("Bob", "12444567")
h.add_values("Bill", "KKKKKKK")

print(h.get_value("Bob"))
h.delete_value("Bob")
print(h.get_value("Bill"))

h.print_all()