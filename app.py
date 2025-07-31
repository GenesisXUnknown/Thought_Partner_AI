from flask import Flask, render_template, request, jsonify
import os
import sys

# Add the current directory to the Python path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from encoder import MultimodalEncoder
    from tti import ThoughtTraceInterpreter
    from plugins import PluginInterface
    from memory import ReasoningMemory
    from explainability import ExplainabilityLayer
except ImportError:
    # If the original modules fail, we'll create mock implementations
    print("Warning: Could not import AI modules, using mock implementations")
    
    class MultimodalEncoder:
        def encode(self, inputs):
            return {"encoded": f"Encoded: {inputs.get('text', 'No text provided')}"}
    
    class ThoughtTraceInterpreter:
        def interpret(self, encoded):
            return {"interpretation": "Analyzed multimodal input", "confidence": 0.85}
    
    class PluginInterface:
        def __init__(self):
            pass
    
    class ReasoningMemory:
        def update(self, trace):
            pass
    
    class ExplainabilityLayer:
        def generate_cards(self, trace):
            return [
                {"title": "Input Analysis", "content": "The system processed your input successfully"},
                {"title": "Reasoning", "content": "Applied multimodal analysis techniques"},
                {"title": "Confidence", "content": f"Analysis confidence: {trace.get('confidence', 'N/A')}"}
            ]

app = Flask(__name__)

# Initialize AI components
encoder = MultimodalEncoder()
tti = ThoughtTraceInterpreter()
plugins = PluginInterface()
memory = ReasoningMemory()
explain = ExplainabilityLayer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        text_input = data.get('text', '')
        
        if not text_input:
            return jsonify({'error': 'Please provide text input'}), 400
        
        # Process the input through our AI pipeline
        inputs = {"text": text_input}
        encoded = encoder.encode(inputs)
        trace = tti.interpret(encoded)
        memory.update(trace)
        cards = explain.generate_cards(trace)
        
        return jsonify({
            'success': True,
            'trace': trace,
            'explanation_cards': cards,
            'processed_input': text_input
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'Thought Partner AI is running'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))