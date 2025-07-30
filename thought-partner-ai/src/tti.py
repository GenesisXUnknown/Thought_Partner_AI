class ThoughtTraceInterpreter:
    def interpret(self, encoded):
        return [f"Step({k})" for k in encoded]
