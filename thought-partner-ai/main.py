"""Main Driver Script
Demonstrates interaction between core components.
"""
from encoder import MultimodalEncoder
from tti import ThoughtTraceInterpreter
from plugins import PluginInterface
from memory import ReasoningMemory
from explainability import ExplainabilityLayer

if __name__ == "__main__":
    encoder = MultimodalEncoder()
    tti = ThoughtTraceInterpreter()
    plugins = PluginInterface()
    memory = ReasoningMemory()
    explain = ExplainabilityLayer()

    inputs = {"text": "What is photosynthesis?", "image": "leaf_diagram.png"}
    encoded = encoder.encode(inputs)
    trace = tti.interpret(encoded)
    memory.update(trace)
    cards = explain.generate_cards(trace)

    print("Trace:", trace)
    print("Explainability Cards:", cards)
