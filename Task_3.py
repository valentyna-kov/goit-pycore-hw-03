import re


def normalize_phone(phone_number:str)->str:
    """
    Returns the phone numbers in the normalized format +380XXXXXXXXX. If the format is not correct, then returns an empty value
    
    Args:
        phone_number (str): The phone number string in different formats.
    Returns:
        str: 
        - if the input number is valid, then the normalized phone number format '+380XXXXXXXXX' is returned;
        - if the input number is invalid, then the empty value is returned.
    """
    raw_phone = re.sub(r'[^\d+]', '', phone_number)
    if raw_phone.startswith('+'):
        normalized_phone = raw_phone
    elif raw_phone.startswith('380'):
        normalized_phone = '+' + raw_phone
    elif raw_phone.startswith('80'):
        normalized_phone = '+3' + raw_phone
    else:
        normalized_phone = '+38' + raw_phone

    #check the phone number format for correctnes
    if len(normalized_phone) != 13 or normalized_phone.count('+') > 1:
        # wrong phone number format
        normalized_phone =""

    return normalized_phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)