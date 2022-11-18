import interpreter


class Application:
    def __init__(self):
        self.interpreter = interpreter.Interpreter()
        self.run = False

    def execute(self):
        while self.get_is_to_run():
            self.procedure()

    def procedure(self):
        pass

    def get_is_to_run(self):
        return self.run

    def set_is_to_run(self, v):
        self.run = bool(v)

