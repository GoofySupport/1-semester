#binær omregner
def int_to_bin_converter(value):
    return f"{value:06b}"

#decimal tals omregner.
def int_to_float_converter(value):
    return float(value)

#heltal til romeresk tal
def int_to_roman_converter(value):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC",
           "C", "CD", "D", "CM", "M"]

    result = ""

    i = len(num) - 1
    while value:
        div = value // num[i]
        value %= num[i]

        while div:
            result += sym[i]
            div -= 1
        i -= 1

    return result


def roman_to_int_converter(value):
    """Roman to integer converter"""
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(value)):
        if i > 0 and rom_val[value[i]] > rom_val[value[i - 1]]:
            int_val += rom_val[value[i]] - 2 * rom_val[value[i - 1]]
        else:
            int_val += rom_val[value[i]]
    return int_val


"""Main Converter Code"""
user_input = int(input("Choose a number between 1 and 3."
                       "\n\t(1) to access the binary converter"
                       "\n\t(2) to access the float converter"
                       "\n\t(3) to access the roman numerals\n"))

if isinstance(user_input, int):
    if user_input == 3:
        user_input = int(input("Please enter a number that is either 1 or 2."
                               "\n\t(1) to convert from integer to roman"
                               "\n\t(2) to convert from roman to integer\n"))

        if user_input == 1:
            numb_to_convert = int(input("Please enter an integer you want to convert: "))
            print(f"You chose number {numb_to_convert} which in roman numerals is "
                  f"{int_to_roman_converter(numb_to_convert)}")
        elif user_input == 2:
            numb_to_convert = input("Please enter a roman number you want to convert: ")
            print(f"You chose roman number {numb_to_convert.upper()} which is "
                  f"{roman_to_int_converter(numb_to_convert.upper())}")
    else:
        numb_to_convert = int(input("Please enter an integer you want to convert: "))
        if user_input == 1:
            print(f"You chose number {numb_to_convert} which in binary is {int_to_bin_converter(numb_to_convert)}")
        elif user_input == 2:
            print(f"You chose number {numb_to_convert} which in float is {int_to_float_converter(numb_to_convert)}")

else:
    print(f"You failed to enter a number between 1 and 3.")