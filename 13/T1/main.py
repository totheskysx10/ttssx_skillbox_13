class Square:
    def __init__(self, count):
        self.start_num = 0
        self.count = count

    def __iter__(self):
        self.start_num = 0
        return self

    def __next__(self):
        while self.start_num < self.count:
            self.start_num += 1
            return self.start_num ** 2
        raise StopIteration

def get_nums_square(count):
    for num in range(1, count + 1):
        yield num ** 2

class_iterator = Square(10)
generator = get_nums_square(10)
gen_exp = (num ** 2 for num in range(1, 11))

for current in class_iterator:
    print(current)
print()

for current in generator:
    print(current)
print()

for current in gen_exp:
    print(current)