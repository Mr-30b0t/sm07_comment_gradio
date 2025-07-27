import gradio as gr
from helpers import validate_dates

def calculate_service_units(start, end):
    """Calculate days and service units based on date range."""
    try:
        from datetime import datetime
        d1 = datetime.strptime(start.strip(), '%m/%d/%Y')
        d2 = datetime.strptime(end.strip(), '%m/%d/%Y')
        delta = (d2 - d1).days + 1

        if delta <= 0:
            gr.Warning("End date must be after start date.")
            return

        if delta == 180:
            units = "Exactly 180 days — 6 service units"
        elif delta > 180:
            units = "6 and excess dates in INFO status"
        else:
            units = f"{(delta - 1) // 30 + 1} service unit(s)"

        gr.Info(f"{delta} day(s)\n{units}")

    except ValueError:
        gr.Warning("Please enter valid dates in MM/DD/YYYY format.")

def generate_comment(portal_id, fax, age, procedure, dx, start_date, end_date, decision, policy_month, initial):
    """Generate the formatted comment based on all inputs."""
    start, end, error = validate_dates(start_date, end_date)
    
    if error:
        return error

    return f"""Portal ID: {portal_id} Fax #: {fax} \
Client is eligible. Duplicates/history checked — none found. \
Provider is eligible. Provider type: 44. No current or future PDC. \
Submitter certification page submitted & completed. \
Requested {', '.join(procedure)} for DOS: {start_date}–{end_date}. \
Client age: {age}. Client has a qualifying condition: {', '.join(dx)} with at least 1 risk factor listed in policy. \
DOS {start_date}–{end_date} is approved based on the Texas Medicaid Medical Policy Manual — {policy_month} Telemonitoring Services and SOP 111. {initial}""" 