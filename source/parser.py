from source.token \
    import Token

from source.custom.stringBuffer \
    import StringBuffer

from source.custom.counter \
    import Counter


class Parser:
    def __init__(self):
        self.token = None

    def init(self):
        if self.token is None:
            self.token = Token()

    def parse(self, str):
        self.init()

        buffer = StringBuffer()

        size_of_str = len(str)
        last = (size_of_str - 1)

        jumps = Counter()

        for id in range(0, size_of_str):
            e = str[id]

            buffer.append(e)
            buffer.append_space()

            if e == ' ' or id == last:
                index = jumps.get_value()
                token_value = buffer.get_value()

                self.evaluate(index, token_value)

                jumps.next()
                buffer.clear()

    def evaluate(self, indexPosition, str_token):
        if indexPosition == 0:
            self.token.set_key(str_token)
        else:
            self.token.append_value(str_token)

    def get_token(self):
        self.init()
        return self.token

    def set_token(self, token):
        self.init()
        self.token = token
