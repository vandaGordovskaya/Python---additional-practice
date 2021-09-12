class MyIterator:
    def __init__(self, iterations):
        self.iter = iterations
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter > 0:
            self.value += 10
            self.iter -= 1
            return self.value
        else:
            raise StopIteration
