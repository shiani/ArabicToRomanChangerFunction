def to_roman_numeral(value: int) -> str:
    """
    Converts an integer value to a Roman numeral.

    Args:
        value (int): The integer value to be converted.

    Returns:
        str: The Roman numeral representation of the input value.

    Raises:
        ValueError: If the input value is not an integer or is outside the range 0 to 3999.

    """

    # Check the value type and range
    if not isinstance(value, int) or not (0 <= value < 4000):
        raise ValueError("value must be an integer number between 0 and 3999")

    # Roman numbers map dictionary sorted from largest to smallest
    roman_numbers_map = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    result = ""

    # Iterate through the roman_numbers_map in descending order
    for num, roman_digit in roman_numbers_map.items():
        # Repeat the current Roman digit until the value is less than the current number
        while value >= num:
            result += roman_digit
            value -= num

    return result
