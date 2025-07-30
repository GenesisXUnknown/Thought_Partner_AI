"""Dialogue Memory
Stores longitudinal context across multiple reasoning steps.
"""

class ReasoningMemory:
    def __init__(self):
        self.memory = []

    def update(self, trace):
        self.memory.append(trace)

    def retrieve(self):
        return self.memory
