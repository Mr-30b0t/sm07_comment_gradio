from datetime import datetime
import gradio as gr

# Function to normalize flexible date formats
def normalize_date(date_str):
    formats = ["%m/%d/%Y", "%Y-%m-%d", "%d-%m-%Y", "%m-%d-%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt).date()
        except ValueError:
            continue
    return None

# Function to calculate days and service units
def check_date(start, end):
    try:
        d1 = datetime.strptime(start.strip(), '%m/%d/%Y')
        d2 = datetime.strptime(end.strip(), '%m/%d/%Y')
        delta = (d2 - d1).days + 1

        if delta <= 0:
            gr.Warning("❌ End date must be after start date.")
            return

        if delta == 180:
            units = "Exactly 180 days — 6 days"
        elif delta > 180:
            units = "6 and INFO detail"
        else:
            units = f"{(delta - 1) // 30 + 1} service unit(s)"

        gr.Info(f"📆 {delta} day(s)\n🧾 {units}")

    except ValueError:
        gr.Warning("❌ Please enter valid dates in MM/DD/YYYY format.")

# Function to generate the comment
def copy_action(portal_id, fax, age, procedure, dx, start_date, end_date, decision, policy_month, initial):
    start = normalize_date(start_date)
    end = normalize_date(end_date)

    if not start or not end:
        return "❌ Invalid date format. Please use MM/DD/YYYY or YYYY-MM-DD."

    if start > end:
        return "❌ End date must be after or equal to start date."

    return f"""Portal ID: {portal_id} Fax #: {fax} \
Client is eligible. Duplicates/history checked — none found. \
Provider is eligible. Provider type: 44. No current or future PDC. \
Submitter certification page submitted & completed. \
Requested {', '.join(procedure)} for DOS: {start_date}–{end_date}. \
Client age: {age}. Client has a qualifying condition: {', '.join(dx)} with at least 1 risk factor listed in policy. \
DOS {start_date}–{end_date} is approved based on the Texas Medicaid Medical Policy Manual — {policy_month} Telemonitoring Services and SOP 111. {initial}"""

# Interface with a custom theme from HuggingFace Hub
with gr.Blocks(theme='JohnSmith9982/small_and_pretty') as demo:
    gr.Markdown("# SM07 Comment Generator")
    with gr.Row(variant="panel"):
        copy_btn = gr.Button("Generate Comment", size="sm")

    with gr.Tab("🧑‍⚕️ Client Info"):
        with gr.Row():
            portal_id = gr.Textbox(label="Portal ID", lines=1, max_lines=1, scale=1)
            fax = gr.Textbox(label="Fax #", lines=1)
            age = gr.Textbox(label="Client Age", lines=1)

        procedure = gr.CheckboxGroup(choices=["S9110", "S9110-U1"], label="Procedure Code(s)")
        dx = gr.CheckboxGroup(choices=["Hypertension", "Diabetes"], label="Diagnosis (DX)")

    with gr.Tab("📅 Request Details"):
        with gr.Row():
            start_date = gr.Textbox(label="Start Date (MM/DD/YYYY)")
            end_date = gr.Textbox(label="End Date (MM/DD/YYYY)")

        check_days_btn = gr.Button("🧮 Check Days")

        decision = gr.Radio(choices=["Approved"], value="Approved", label="Decision Type")

        with gr.Row():
            clear_btn = gr.Button("🧹 Clear Output")

    with gr.Tab("Misc."):
        with gr.Row():
            initial = gr.Textbox(label="Nurse Initials")
            policy_month = gr.Textbox(label="Policy month/year")

    output = gr.Textbox(label="💬 Generated Output", lines=12, interactive=False, show_copy_button=True)

    # Button logic
    copy_btn.click(fn=copy_action,
                inputs=[portal_id, fax, age, procedure, dx, start_date, end_date, decision, policy_month, initial],
                outputs=output)

    check_days_btn.click(fn=check_date, inputs=[start_date, end_date], outputs=[])
    clear_btn.click(fn=lambda: "", inputs=[], outputs=output)

demo.launch()
