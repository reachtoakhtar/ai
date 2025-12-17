__author__ = "akhtar"


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None] * self.MAX

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index]

class HashTableSeparateChaining (HashTable):
    def __init__(self):
        super().__init__()
        self.arr = [[] for i in range(self.MAX)]

class HashTableLinearProbing (HashTable):
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = val
        else:
            while True:
                start = h
                i = start + 1
                print(f'i: {i}')

                if i == start:  # reached starting point again → stop
                    break
                else:
                    if self.arr[i] is None:
                        self.arr[i] = val
                        break
                    i = (i + 1) % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        return self.arr[arr_index]

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        del self.arr[arr_index]
