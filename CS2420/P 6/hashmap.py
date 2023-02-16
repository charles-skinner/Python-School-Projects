"""
docstring
"""

class Node:
    """
    docstring
    """
    def __init__(self,key=None,weight=None):
        self.key = key
        self.weight = weight
        self.next = None


class HashMap:
    """
    docstring
    """
    def __init__(self,cap=7):
        self.cap = cap
        self.buckets = []
        for _ in range(self.cap):
            self.buckets.append(None)


    def get(self,key):
        """
        Return the value for key if key is in the dictionary. If key is not in the
        dictionary, raise a KeyError.
        """
        current = self.buckets[self.hash(key)]
        while current is not None:
            if current.key == key:
                return current.weight
            current = current.next
        raise KeyError


    def set(self,key, value):
        """
        add the (key,value) pair to the hashMap. After adding, if the load-
        factor >= 80%, rehash the map into a map double its current capacity.
        """
        node = Node(key,value)
        index = self.hash(key)
        current = self.buckets[index]
        if current is None:
            self.buckets[index] = node
        elif current.key == key:
            current.weight = value
        else:
            while current.next is not None:
                if current.key == key:
                    current.weight = value
                    break
                current = current.next
            current.next = node
        #check load factor
        load_factor = self.size()/self.capacity()
        if load_factor >= 0.8:
            store = []
            for keey in self.keys():
                store.append([keey,self.get(key)])
            self.cap = (self.cap*2)-1
            self.clear(self.cap)
            for pair in store:
                self.set(pair[0],pair[1])


    def remove(self,key):
        """
        Remove the key and its associated value from the map. If the key
        does not exist, nothing happens. Do not rehash the table after deleting keys.
        """
        try:
            self.get(key)
        except:
            raise KeyError
        index = self.hash(key)
        current = self.buckets[index]
        if current.key == key:
            self.buckets[index] = current.next
            return
        while current.next.key != key:
            current = current.next
        current.next = current.next.next


    def clear(self,cap=7):
        """
        empty the HashMap
        """
        # for i in range(self.cap):
        #     self.buckets[i] = None
        self.__init__(cap) #i think this one is better, but kept old method for reference


    def capacity(self):
        """
        Return the current capacity--number of buckets--in the map.
        """
        return self.cap


    def size(self):
        """
        Return the number of key-value pairs in the map.
        """
        size = 0
        for i in range(self.cap):
            if self.buckets[i]:
                size += 1
        return size


    def keys(self):
        """
        Return a list of keys.
        """
        keys = []
        for i in range(self.cap):
            current = self.buckets[i]
            while current:
                keys.append(current.key)
                current = current.next
        return keys


    def hash(self,key):
        """
        docstring
        """
        return int(str(key[0])+str(key[1]))%self.cap
        