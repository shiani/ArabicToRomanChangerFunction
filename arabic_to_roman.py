from enum import Enum

class RomanNumerals(Enum):
    M = 1000
    CM = 900
    D = 500
    CD = 400
    C = 100
    XC = 90
    L = 50
    XL = 40
    X = 10
    IX = 9
    V = 5
    IV = 4
    I = 1

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

    result = []

    # Iterate through the RomanNumerals Enum in descending order
    for numeral in RomanNumerals:
        while value >= numeral.value:
            result.append(numeral.name)
            value -= numeral.value

    return ''.join(result)
