import gradio as gr
from comment_generator import generate_comment, calculate_service_units

# Load CSS
with open("style.css", "r") as f:
    css = f.read()

# Interface with custom theme
with gr.Blocks(css=css) as demo:
    gr.Markdown("# SM07 Comment Generator")
    
    with gr.Tab("Client Info"):
        with gr.Row():
            portal_id = gr.Textbox(label="Portal ID", lines=1, max_lines=1, scale=1)
            fax = gr.Textbox(label="Fax #", lines=1)

        with gr.Row():
            age = gr.Textbox(label="Client Age", lines=1)
            dx = gr.CheckboxGroup(choices=["HTN", "DM"], label="DX")
        procedure = gr.CheckboxGroup(choices=["S9110", "S9110-U1"], label="Procedure Code(s)")
        

    with gr.Tab("Request Dates"):
        with gr.Row():
            start_date = gr.Textbox(label="Start Date")
            end_date = gr.Textbox(label="End Date")

        check_days_btn = gr.Button("Check Days", size="sm")

        decision = gr.Radio(choices=["Approved"], value="Approved", label="Decision Type")

    with gr.Tab("Settings"):
        with gr.Row():
            initial = gr.Textbox(label="Nurse Initials")
            policy_month = gr.Textbox(label="Policy month/year")

    with gr.Row(variant="panel"):
        copy_btn = gr.Button("Generate Comment", size="sm")

    output = gr.Textbox(label="Generated Output", lines=12, interactive=False, show_copy_button=True)

    # Button logic
    copy_btn.click(fn=generate_comment,
                inputs=[portal_id, fax, age, procedure, dx, start_date, end_date, decision, policy_month, initial],
                outputs=output)

    check_days_btn.click(fn=calculate_service_units, inputs=[start_date, end_date], outputs=[])

if __name__ == "__main__":
    demo.launch() 