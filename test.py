import gradio as gr

css = """
body {
    background-color: red !important;
}
"""

with gr.Blocks(css=css) as demo:
    gr.Textbox(label="Test Input")
    gr.Button("Click Me")

demo.launch()