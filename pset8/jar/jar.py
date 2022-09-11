"""
USAGE:
$ python jar.py

DESCRIPTION:
Implement a cookie jar in which to store cookies. This is a class with methods:
- __init__: Initialize a cookie jar with a given capacity, which represents the maximum number of cookies
            that can fit in the cookie jar.
            If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
- __str__:  Return a str with  🍪, where  is the number of cookies in the cookie jar.
            For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
- deposit:  add n cookies to the cookie jar.
            If adding that many would exceed the cookie jar's capacity, though,
            deposit should instead raise a ValueError.
- withdraw: Remove n cookies from the cookie jar.
            If there aren't that many cookies in the cookie jar, though,
            withdraw instead raise a ValueError.
- capacity (getter): Return the cookie jar's capacity.
- capacity (setter): Set the jar's capacity.
- size (getter): Return the number of cookies actually in the cookie jar.
- size (setter): Set the number of cookies.
"""

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Negative capacity!")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        """Add n cookies to the current cookies"""
        if self._size + n > self._capacity:
            raise ValueError("Beyond capacity! 😵")
        self.size += n

    def withdraw(self, n):
        """Remove n cookies from the current cookies"""
        if self.size - n < 0:
            raise ValueError("Not Enough cookies! 😭")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Negative capacity?! 😱")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Negative cookies?! 🤡")
        self._size = size

def main():
    jr = Jar()

    jr.deposit(12)
    print(jr.capacity)
    print(jr.size)

    jr.withdraw(7)
    print(jr.capacity)
    print(jr.size)


if __name__ == "__main__":
    main()