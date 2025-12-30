import gradio as gr

def greet(name):
    if name.strip() == "":
        return "Please enter a name 😊"
    return f"Hello {name}! 👋"

iface = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="My First HuggingFace Web App",
    description="Enter your name and say hello!"
)

if __name__ == "__main__":
    iface.launch()
