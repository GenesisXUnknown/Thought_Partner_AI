"""Explainability Layer
Produces human-readable cards summarizing reasoning.
"""

class ExplainabilityLayer:
    def generate_cards(self, trace):
        return [f"Explain: {step}" for step in trace]
