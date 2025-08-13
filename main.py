import gradio as gr
from config import CSS_FILE_PATH, APP_TITLE, SHARE_APP
from ui_components import (
    create_client_info_tab, 
    create_dates_tab, 
    create_settings_tab, 
    create_stats_tab,
    create_output_section
)
from event_handlers import setup_event_handlers

def load_css():
    """Load CSS from file."""
    try:
        with open(CSS_FILE_PATH, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Warning: CSS file {CSS_FILE_PATH} not found. Using default styling.")
        return ""

def create_interface():
    """Create the main Gradio interface."""
    css = load_css()
    
    with gr.Blocks(css=css) as demo:
        gr.Markdown(f"# {APP_TITLE}")
        
        # Create UI components
        portal_id, fax, age, dx, procedure = create_client_info_tab()
        start_date, end_date, check_days_btn, decision = create_dates_tab()
        initial, policy_month = create_settings_tab()
        stats_btn, reset_btn, stats_output = create_stats_tab()
        copy_btn, output = create_output_section()
        
        # Setup event handlers
        setup_event_handlers(
            copy_btn, check_days_btn, output,
            portal_id, fax, age, procedure, dx,
            start_date, end_date, decision, policy_month, initial,
            stats_btn, reset_btn, stats_output
        )
        
        return demo

def main():
    """Main application entry point."""
    demo = create_interface()
    demo.launch(share=SHARE_APP)

if __name__ == "__main__":
    main()