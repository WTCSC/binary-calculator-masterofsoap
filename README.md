# Binary Calculator

## Overview

The **Binary Calculator** is a Python-based utility that performs basic arithmetic operations (`+`, `-`, `*`, `/`) on binary numbers. It ensures proper handling of binary inputs, performs accurate conversions between binary and decimal representations, and returns results as 8-bit binary strings.

The calculator also includes robust error handling for invalid inputs, overflow conditions, and division by zero.

---

## Features

- **Arithmetic Operations**: Supports addition, subtraction, multiplication, and integer division.
- **Input Validation**: Ensures inputs contain only valid binary digits (`0` and `1`).
- **Error Handling**:
  - Returns `"Error"` for invalid binary inputs or operators.
  - Returns `"NaN"` for division by zero.
  - Returns `"Overflow"` if the result exceeds the 8-bit range (0 to 255).
- **Output Format**: Results are always returned as 8-bit binary strings (padded with leading zeros).

---

## Requirements

- Python 3.x
- No external libraries are required.

---

## Usage

### Function Signature

```python
def binary_calculator(bin1, bin2, operator):
    """
    Perform arithmetic operations on two binary numbers.
    
    Parameters:
    - bin1 (str): First binary number (string of 0s and 1s).
    - bin2 (str): Second binary number (string of 0s and 1s).
    - operator (str): Arithmetic operator ('+', '-', '*', '/').

    Returns:
    - str: Result as an 8-bit binary string or an error message.
    """
```

### Example Usage

```python
# Import the function (if saved in a separate file)
from binary_calculator import binary_calculator

# Example test cases
print(binary_calculator("1010", "1010", "+"))  # Output: "00010100"
print(binary_calculator("1100", "0011", "-"))  # Output: "00001001"
print(binary_calculator("1010", "0000", "/"))  # Output: "NaN"
print(binary_calculator("1010", "abc", "+"))   # Output: "Error"
```

---

## Implementation Details

### Input Validation
- Both `bin1` and `bin2` must be strings containing only `0` and `1`.
- The `operator` must be one of the supported arithmetic operators: `+`, `-`, `*`, `/`.

### Binary-to-Decimal Conversion
- Custom logic converts binary strings to their decimal equivalents using positional values (\(2^i\)).

### Decimal-to-Binary Conversion
- Results are converted back to binary using repeated division by 2.
- The binary string is padded with leading zeros to ensure it is 8 bits long.

### Error Handling
- **Invalid Inputs**: Returns `"Error"` if `bin1` or `bin2` contains invalid characters.
- **Division by Zero**: Returns `"NaN"`.
- **Overflow**: If the result exceeds the range of an 8-bit number (0-255), `"Overflow"` is returned.

---

## Edge Cases

| Input                             | Output       | Reason                   |
|-----------------------------------|--------------|--------------------------|
| `"1010"`, `"1010"`, `"+"`         | `"00010100"` | Valid addition           |
| `"1100"`, `"0011"`, `"-"`         | `"00001001"` | Valid subtraction         |
| `"1010"`, `"0000"`, `"/"`         | `"NaN"`      | Division by zero         |
| `"1010"`, `"abc"`, `"+"`          | `"Error"`    | Invalid binary input     |
| `"11111111"`, `"00000001"`, `"+"` | `"Overflow"` | Result exceeds 8 bits    |

---

## Testing

To test the `binary_calculator` function, create a Python file with test cases and call the function with various inputs. Example test cases are provided above.

---

