import gradio as gr
from config import DIAGNOSIS_CHOICES, PROCEDURE_CHOICES, DECISION_CHOICES, DEFAULT_DECISION

def create_client_info_tab():
    """Create the Client Info tab with all its components."""
    with gr.Tab("Client Info"):
        with gr.Row():
            portal_id = gr.Textbox(label="Portal ID", lines=1, max_lines=1, scale=1)
            fax = gr.Textbox(label="Fax #", lines=1)

        with gr.Row():
            age = gr.Textbox(label="Client Age", lines=1)
            dx = gr.CheckboxGroup(choices=DIAGNOSIS_CHOICES, label="DX")
        
        procedure = gr.CheckboxGroup(choices=PROCEDURE_CHOICES, label="Procedure Code(s)")
        
        return portal_id, fax, age, dx, procedure

def create_dates_tab():
    """Create the Request Dates tab with all its components."""
    with gr.Tab("Request Dates"):
        with gr.Row():
            start_date = gr.Textbox(label="Start Date")
            end_date = gr.Textbox(label="End Date")

        check_days_btn = gr.Button("Check Days", size="sm")
        decision = gr.Radio(choices=DECISION_CHOICES, value=DEFAULT_DECISION, label="Decision Type")
        
        return start_date, end_date, check_days_btn, decision

def create_settings_tab():
    """Create the Settings tab with all its components."""
    with gr.Tab("Settings"):
        with gr.Row():
            initial = gr.Textbox(label="Nurse Initials")
            policy_month = gr.Textbox(label="Policy month/year")
            
        return initial, policy_month

def create_stats_tab():
    """Create the Statistics tab with stats display and reset button."""
    with gr.Tab("Stats"):
        with gr.Row():
            stats_btn = gr.Button("🔄 Refresh Stats", size="sm")
            reset_btn = gr.Button("🗑️ Reset Stats", size="sm", variant="secondary")
        
        stats_output = gr.Markdown("Click 'Refresh Stats' to view statistics.")
        
        return stats_btn, reset_btn, stats_output

def create_output_section():
    """Create the output section with generate button and output textbox."""
    with gr.Row(variant="panel"):
        copy_btn = gr.Button("Generate Comment", size="sm")

    output = gr.Textbox(label="Generated Output", lines=12, interactive=False, show_copy_button=True)
    
    return copy_btn, output
