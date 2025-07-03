import sys


class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError("Too many cookies")
        return self.size

    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError("Cannot remove any more cookies")
        return self.size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity too low")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError
        self._size = size


def main():
    jar = Jar()

    while True:
        interact = input("View cookies by typing 'view', see capacity by typing 'capacity', see how many cookies in the jar by typing 'size',type 'p' to pass or 'e' to exit:\n").strip().lower()

        if interact == "view":
            print(jar)
        elif interact == "capacity":
            print(jar.capacity)
        elif interact == "size":
            print(jar.size)
        elif interact == "p":
            pass
        elif interact == "e":
            sys.exit()
        else:
            raise ValueError("Unknown input")

        interact = input("Add cookies by typing 'add', remove cookies by typing 'eat', or type 'p' to pass:\n").strip().lower()

        if interact == "add":
            n = int(input("Add cookies: "))
            jar.deposit(n)
        elif interact == "eat":
            n = int(input("Eat cookies: "))
            jar.withdraw(n)
        elif interact == "p":
            pass
        else:
            raise ValueError("Unknown input")


if __name__ == "__main__":
    main()
