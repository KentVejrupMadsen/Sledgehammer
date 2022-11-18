class Counter:
    def __init__(self):
        self.n = None

    def init(self):
        if self.n is None:
            self.n = 0

    def next(self):
        self.additive(1)

    def additive(self, n):
        new_val = (self.n + n)
        self.set_value(new_val)

    def substract(self, n):
        new_val = (self.n - n)
        self.set_value(new_val)

    def previous(self):
        self.substract(1)

    def get_value(self):
        self.init()
        return self.n

    def set_value(self, n):
        self.init()
        self.n = n

