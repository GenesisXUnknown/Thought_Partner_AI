class ReasoningMemory:
    def __init__(self):
        self.memory = []
    def update(self, trace):
        self.memory.append(trace)
