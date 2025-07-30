class ExplainabilityLayer:
    def generate_cards(self, trace):
        return [f"Explain: {t}" for t in trace]
