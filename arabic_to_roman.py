def to_roman_numeral(value: int) -> str:

    # check the value type and range
    if type(value) != int or not (0 <= value < 4000):
        raise ValueError("value must be an integer number between 0 and 3999")

    # roman numbers map dictionary sorted from largest to smallest
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

    # [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    for num in roman_numbers_map.keys():

        # find roman string in numbers map
        roman_digit = roman_numbers_map[num]

        # check how many times that value repeated
        # example: 2196 has two 1000 so times is 2
        times = value // num

        # if the value does not include that number we can continue to other numbers
        if times == 0:
            continue

        # new value is remainder of previous value
        # example:  2196 remainder of 1000 is 196 so new value is 196
        value = value % num

        # new result added to previous result
        # example: 2196 has two 1000 so "MM" added to result
        result += roman_digit * times

        if value == 0:
            break

    return result
