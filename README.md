# Interpretable Multimodal Thought-Partner AI

This repository implements a research prototype for a next-generation multimodal AI collaborator. It integrates natural language, visual, and code reasoning with interpretable outputs and plugin-based customization. Designed for scientific co-thinking tasks.

---

## 📘 Abstract

See full paper: [docs/paper.md](./docs/paper.md)

---

## 🔧 Installation

```bash
git clone https://github.com/yourusername/thought-partner-ai.git
cd thought-partner-ai
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python src/main.py
```

Example input:
```python
inputs = {
    "text": "What is photosynthesis?",
    "image": "leaf_diagram.png"
}
```

Expected output:
- Reasoning trace from Thought Trace Interpreter
- Explainability cards with step-by-step rationale

---

## 📁 Project Structure

- `src/` - Core modules (encoder, reasoning, plugins, explainability)
- `docs/` - Paper, diagrams, supporting documentation
- `benchmarks/` - MultiThink benchmark for evaluation

---

## 🔬 Requirements

See `requirements.txt` or install via pip:

```txt
transformers
torch
pillow
matplotlib
scikit-learn
```

---

## 📓 Live Demo Notebook

Open in Colab: [Launch Notebook](https://colab.research.google.com/github/yourusername/thought-partner-ai/blob/main/demo.ipynb)

---

## 📜 License

MIT License

---

## 🤝 Contribution

We welcome contributions from AI researchers, ML engineers, and domain scientists.
