class Numbers:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        raise StopIteration


n = int(input("Enter N: "))

for x in Numbers(n):
    print(x)


class ReverseNumbers:
    def __init__(self, n):
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= 1:
            value = self.current
            self.current -= 1
            return value
        raise StopIteration


n = int(input("Enter N: "))

for x in ReverseNumbers(n):
    print(x)



class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            value = self.current
            self.current += 2
            self.count += 1
            return value
        raise StopIteration


n = int(input("Enter N: "))

for x in EvenNumbers(n):
    print(x)



class OddNumbers:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            value = self.current
            self.current += 2
            self.count += 1
            return value
        raise StopIteration


n = int(input("Enter N: "))

for x in OddNumbers(n):
    print(x)


class EvenList:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1

            if value % 2 == 0:
                return value

        raise StopIteration


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for x in EvenList(numbers):
    print(x)


class OddList:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1

            if value % 2 != 0:
                return value

        raise StopIteration


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for x in OddList(numbers):
    print(x)



class PositiveNumbers:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1

            if value > 0:
                return value

        raise StopIteration


numbers = [-5, 10, -2, 7, 0, 8, -1]

for x in PositiveNumbers(numbers):
    print(x)


class StringIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.text):
            value = self.text[self.index]
            self.index += 1
            return value

        raise StopIteration


text = input("Enter a string: ")

for x in StringIterator(text):
    print(x)



class ReverseString:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            value = self.text[self.index]
            self.index -= 1
            return value

        raise StopIteration


text = input("Enter a string: ")

for x in ReverseString(text):
    print(x)


