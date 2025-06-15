import random


def get_numbers_ticket(min:int, max:int, quantity:int)-> list[int]:
    """
    Reterns list of random numbers in the range [min, max] with elements quantity 

    Args:
        min (int): Minimum range value, must be >= 1
        max (int): Maximum range value, must be <= 1000
        quantity (int): Number of elements in the list. Must be less or equel to 1 AND more or equel to 1000.
    Returns:
        list[int]:
        - if input parameter is valid, then the list of unique random numbers soted in ASC order must be reterned;
        - if input parameter is invalid, the empty list must be reterned
    """
    if min < 1 or max > 1000:
        # The input parameter is invalid. Set up the quentity 1 <= min < max <= 1000
        return []
    elif quantity < 1 or quantity  > (max - min)+1:
        # The invalid input parameter. Set up the quantity within the range.
        return []
    else:
        # Sorted list of unique random numbers
        return sorted(random.sample(range(min, max + 1), quantity))


print(get_numbers_ticket(min=1, max=1000, quantity=4))