from datetime import datetime

def normalize_date(date_str):
    """Normalize flexible date formats to a standard format."""
    formats = ["%m/%d/%Y", "%Y-%m-%d", "%d-%m-%Y", "%m-%d-%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt).date()
        except ValueError:
            continue
    return None

def validate_dates(start_date, end_date):
    """Validate date inputs and return normalized dates."""
    start = normalize_date(start_date)
    end = normalize_date(end_date)
    
    if not start or not end:
        return None, None, "Invalid date format. Please use MM/DD/YYYY or YYYY-MM-DD."
    
    if start > end:
        return None, None, "End date must be after or equal to start date."
    
    return start, end, None 