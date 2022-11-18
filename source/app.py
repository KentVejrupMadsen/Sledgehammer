import interpreter, parser

default_prompt = ' > '


class Application:
    def __init__(self):
        global default_prompt

        self.interpreter = interpreter.Interpreter()
        self.parser = parser.Parser()

        self.run = True

        self.global_prompt = default_prompt

    def execute(self):
        while self.get_is_to_run():
            self.procedure()

    def procedure(self):
        input_str = input(self.global_prompt)
        token = self.parser.parse(input_str)

        if token is not None:
            self.interpreter.decide(token)

    def get_is_to_run(self):
        return self.run

    def set_is_to_run(self, v):
        self.run = bool(v)

