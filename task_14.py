class EvenNumbers:
    def __init__(self, amount) -> None:
        self.amount = amount

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1
        if self.current == self.amount:
            raise StopIteration

        return self.current*2
