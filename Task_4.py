from datetime import datetime, timedelta


def get_upcoming_birthdays(users:list[dict[str,str]]) -> list[dict[str,str]]:
    """
    Returns the list of users with upcoming birthdays in the next 7 days,
    adjusting for leap-year dates and weekend.

    Args:
        users (list[dict[str, str]]): The dictionary with users, with "name" and "birthday" ("YYYY.MM.DD").
    Returns:
        list[dict[str, str]]: The list of dictionaries, with "name" and "congratulation_date" ("YYYY.MM.DD")
                              for birthdays in the next 7 days.
                              - if the birthday date is on weekend, then the congratulation date is shifted to the next Monday.
                              - if February 29 birthday in the 365-day years, the congratulation date is shifted to March 1.
    """
    current_date = datetime.today().date()
    result: list[dict[str, str]] = []  

    for user in users:
        try:
            user_birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        except (KeyError, ValueError, TypeError):
            # If the birthday's format is incorrect OR missing, skip the user
            continue

        try:
            birthday_this_year = user_birthday.replace(year=current_date.year)
        except ValueError:
            # If the birtday in February 29 and the year is not in the 365-day years, shift the congratulation date to March 1
            birthday_this_year = datetime(current_date.year, 3, 1).date()

        if birthday_this_year < current_date:
            try:
                birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)
            except ValueError:   
                # If the birthday in February 29 and the year is not in the 365-day years, shift the congratulation date to March 1
                birthday_this_year = datetime(current_date.year+1, 3, 1).date()

        days_count= (birthday_this_year - current_date).days

        if 0 <= days_count <= 7:
            iso_weekday = birthday_this_year.isoweekday()
            if iso_weekday >= 6: # Saturday or Sunday
                    congratulation_date=birthday_this_year+ timedelta(days= 8 - iso_weekday)
            else:
                    congratulation_date=birthday_this_year

            result.append({"name": user["name"],"congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
    return result

                
users = [
    {"name": "John Doe", "birthday": "1985.06.22"},
    {"name": "Jane Smith", "birthday": "1990.06.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)                     



