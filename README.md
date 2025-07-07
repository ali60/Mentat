# Mentat: Neurofeedback LLM Coding Assistant

**Mentat** is a real-time coding assistant that pairs your Muse EEG device with a large language model (LLM) like GPT-4 to help you code smarter, faster, and more mindfully. It adapts the agent's behavior based on your mental state — boosting creativity, simplifying when you're overloaded, and offering deep reviews when you're focused.

## 🧠 How It Works

- Uses **Muse + Mind Monitor** to stream EEG data (focus, calm, etc.)
- Calculates a **Focus Index** from your brainwaves (beta/alpha ratio)
- Feeds this into an LLM agent (e.g., OpenAI GPT-4)
- LLM adapts its response depending on your current brain state

## 🧪 Features

- Brain-aware prompt adaptation for coding tasks
- Dynamic feedback while you think, design, and debug
- Simple setup with Python + OSC stream

## 🛠 Requirements

- Muse headband
- Mind Monitor app (to stream EEG via OSC)
- Python 3.8+

```bash
pip install python-osc openai numpy
```

## 🚀 Run

1. Connect Muse to Mind Monitor and start streaming OSC to your machine (default port: 5000)
2. Replace the `openai.api_key` in `main.py` with your OpenAI API key
3. Run the app:

```bash
python main.py
```

4. Watch the console for real-time feedback:
   - Focus index based on brain state
   - LLM responses adapted to your cognitive load

## 💡 Example Prompt Adaptation
| Focus Level | LLM Behavior                                |
|-------------|---------------------------------------------|
| High        | Critical code review, deeper architecture  |
| Medium      | Balanced improvement + explanation         |
| Low         | Simplified summary, code walkthroughs      |

## 🧭 Future Ideas
- Use local LLMs via LM Studio or Ollama
- VSCode or Obsidian plugin
- Graphical dashboard for focus tracking
- Speech + audio feedback

## 📄 License
MIT

---

> “The mind commands. The machine obeys.” — *Mentat Philosophy*
