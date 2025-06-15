from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Returns the number of days from current date to specified one

    Args:
        date (str): Date format 'YYYY-MM-DD' 
    Returns:
        int: The difference in days between the current date and the specified one
            - if the date is passed, then the positive value returns;
            - if the date is not passed, then the negative value returns;
            - if the date is invalid, then returns None. 
    """
    try:
        # Set up the input date string into a datetime object
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        # Parameter data must be a string in the format "YYYY-MM-DD")
        return None
    # Get current date
    current_date = datetime.today().date()
    return (current_date - date_obj).days

print(get_days_from_today("2025-06-01"))
