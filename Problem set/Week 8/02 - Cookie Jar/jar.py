class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Capacity should be a non-negative integer') 
        elif type(capacity) != int:
            raise ValueError('Capacity should be a non-negative integer') 
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * '🍪'

    
    def deposit(self, n):
        if type(n) != int:
            raise ValueError('Capacity should be a non-negative integer')
        elif n + self.size> self.capacity:
            raise ValueError('Exceed capacity')
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError('Not enougth cookies in the jar')
        elif type(n) != int:
            raise ValueError('Capacity should be a non-negative integer')
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


one_jar = Jar(15)
one_jar.deposit(4)
one_jar.withdraw(1)
print(one_jar)