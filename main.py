
from pythonosc import dispatcher, osc_server
import numpy as np
import openai
import threading

# --- CONFIGURATION ---
OSC_IP = "0.0.0.0"  # Listen on all interfaces
OSC_PORT = 5000     # Default port Mind Monitor streams to

# Insert your OpenAI API key here
openai.api_key = "your-api-key-here"

# Store EEG data in short rolling windows
alpha_values = []
beta_values = []

def get_code_snippet():
    """
    Replace this with a real snippet from your editor or clipboard.
    For demo, a simple Python function:
    """
    return """
def calculate_tax(price, tax_rate):
    return price * tax_rate
"""

def generate_adaptive_prompt(code_snippet, focus_level):
    """
    Generate prompt based on brain focus level.
    """
    if focus_level > 1.5:
        prompt = f"Critically review this code and suggest advanced improvements:\n{code_snippet}"
    elif focus_level < 0.8:
        prompt = f"Explain this code clearly with simple examples:\n{code_snippet}"
    else:
        prompt = f"Give clean suggestions and explain edge cases for this code:\n{code_snippet}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"LLM Error: {str(e)}"

def eeg_handler(address, *args):
    global alpha_values, beta_values

    # For Muse via Mind Monitor OSC, relative alpha and beta are at indices 3-6 (tweak if needed)
    alpha = np.mean(args[3:5])
    beta = np.mean(args[5:7])

    alpha_values.append(alpha)
    beta_values.append(beta)

    if len(alpha_values) > 10:
        alpha_mean = np.mean(alpha_values[-10:])
        beta_mean = np.mean(beta_values[-10:])
        focus_index = beta_mean / (alpha_mean + 1e-6)

        print(f"\nFocus Index (Beta/Alpha): {focus_index:.2f}")

        code = get_code_snippet()
        llm_response = generate_adaptive_prompt(code, focus_index)

        print("\nLLM Response:\n", llm_response)

def start_server():
    disp = dispatcher.Dispatcher()
    # OSC address for relative alpha and beta from Mind Monitor:
    disp.map("/muse/elements/alpha_relative", eeg_handler)

    server = osc_server.ThreadingOSCUDPServer((OSC_IP, OSC_PORT), disp)
    print(f"[✓] Listening for OSC data on {OSC_IP}:{OSC_PORT} ...")
    server.serve_forever()

if __name__ == "__main__":
    threading.Thread(target=start_server).start()
