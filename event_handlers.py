from comment_generator import generate_comment, calculate_service_units, get_stats, reset_stats

def setup_event_handlers(copy_btn, check_days_btn, output, 
                        portal_id, fax, age, procedure, dx, 
                        start_date, end_date, decision, policy_month, initial,
                        stats_btn, reset_btn, stats_output):
    """Setup all event handlers for the application."""
    
    # Generate comment button handler
    copy_btn.click(
        fn=generate_comment,
        inputs=[portal_id, fax, age, procedure, dx, start_date, end_date, decision, policy_month, initial],
        outputs=output
    )

    # Check days button handler
    check_days_btn.click(
        fn=calculate_service_units, 
        inputs=[start_date, end_date], 
        outputs=[]
    )
    
    # Statistics handlers
    stats_btn.click(
        fn=get_stats,
        inputs=[initial],  # Pass current nurse initials
        outputs=stats_output
    )
    
    reset_btn.click(
        fn=reset_stats,
        inputs=[],
        outputs=stats_output
    )
