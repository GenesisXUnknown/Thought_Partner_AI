class MultimodalEncoder:
    def encode(self, inputs):
        return {k: f"Encoded({k})" for k in inputs}
