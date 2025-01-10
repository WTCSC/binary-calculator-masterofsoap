def binary_calculator(bin1, bin2, operator):
    # Primary Functions
    def is_valid_binary(bin_str): # Makes sure a string is a valid birary number
        return all(char in "01" for char in bin_str)

    def binary_to_decimal(bin_str): # Converts a binary string to a decimal
        decimal = 0
        for i, bit in enumerate(reversed(bin_str)):
            decimal += int(bit) * (2 ** i)
        return decimal

    def decimal_to_binary(decimal): # Converts a decimal to a binary string
        if decimal < 0 or decimal > 255:
            return "Overflow"
        binary = ""
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal //= 2
        return binary.rjust(8, '0')  # Ensure 8-bit representation

    # Validates inputs
    if not (is_valid_binary(bin1) and is_valid_binary(bin2)):
        return "Error"

    # Converts binary inputs to decimals
    decimal1 = binary_to_decimal(bin1)
    decimal2 = binary_to_decimal(bin2)

    # Performs the operation
    try:
        if operator == "+":
            result = decimal1 + decimal2
        elif operator == "-":
            result = decimal1 - decimal2
        elif operator == "*":
            result = decimal1 * decimal2
        elif operator == "/":
            if decimal2 == 0:
                return "NaN"
            result = decimal1 // decimal2
        else:
            return "Error"  # Invalid operator
    except OverflowError:
        return "Overflow"

    # Converts result to binary and returns
    return decimal_to_binary(result)

# Example tests
print(binary_calculator("1010", "1010", "+"))  # Should return "Overflow"
print(binary_calculator("1100", "0011", "-"))  # Should return "00001001"
print(binary_calculator("1010", "0000", "/"))  # Should return "NaN"
print(binary_calculator("1010", "abc", "+"))   # Should return "Error"