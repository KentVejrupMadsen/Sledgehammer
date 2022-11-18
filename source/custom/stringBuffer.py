
class StringBuffer:
    def __init__(self):
        self.created = False
        self.buffer = None

    def clear(self):
        self.buffer = ''

    def init(self):
        if self.buffer is None:
            self.buffer = str()
            self.created_string()

    def append_space(self):
        self.append(' ')

    def append_space_iterate(self, n):
        b = ''

        for i in range(0, n):
            b = b + ' '

        self.append(b)

    def append(self, value):
        if self.is_not_created():
            self.init()

        self.buffer = self.buffer + value

    def get_value(self):
        return self.buffer

    def set_value(self, value):
        self.buffer = value

    def get_is_created(self):
        return self.created

    def set_is_created(self, val):
        self.created = bool(val)

    def is_not_created(self):
        return self.created is False

    def created_string(self):
        self.created = True
