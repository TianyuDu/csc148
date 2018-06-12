"""
Mar26 2018
"""


class HastTable:
    
    def __init__(self):
        pass
    
    def __getitem__(self)
    
    def __setitem__(self, key: object, value: object) -> None:
        """
        >>> ht = HashTable(2)
        >>> ht.capacity == 2
        True
        >>> ht.__setitem__("one", 1)
        >>> ht["two"] = 2
        >>> ht.capacity
        4
        """
        bucket = self.table[hash(key) % self.capacity]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
        if (key, value) not in bucket:
            bucket.append((key, value))
            self.item += 1
            if len(bucket) > 1: 
                self.collisions += 1
        