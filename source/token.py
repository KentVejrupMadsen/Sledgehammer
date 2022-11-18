class Token:
    def __init__(self):
        self.key = None
        self.values = None

    def get_key(self):
        return self.key

    def set_key(self, value):
        self.key = str(value)

    def get_values(self):
        return self.values

    def set_values(self, value):
        self.values = value