class Token:
    def __init__(self):
        self.key = None
        self.values = None

    def append_value(self, value):
        self.init()
        self.values.append(value)

    def get_key(self):
        return self.key

    def set_key(self, value):
        self.key = str(value)

    def get_values(self):
        return self.values

    def set_values(self, value):
        self.values = value

    def init(self):
        if self.values is None:
            self.set_values([])
