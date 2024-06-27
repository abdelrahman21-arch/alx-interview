Certainly! Here is the complete `README.md` in markdown format suitable for GitHub:

```markdown
# UTF-8 Validation

## Description

This project contains a Python script that validates whether a given dataset represents valid UTF-8 encoding. UTF-8 is a variable-width character encoding used for electronic communication. The script checks the dataset to ensure it conforms to the UTF-8 encoding rules.

## Files

- `utf8_validation.py`: The main Python script containing the UTF-8 validation logic.

## Function Prototype

```python
def validUTF8(data):
    """
    Args:
        data: A list of integers representing bytes of data to be validated.

    Returns:
        True if the data is valid UTF-8 encoding, else False.
    """
```

## Usage

1. Ensure you have Python installed on your system.
2. Save the script as `utf8_validation.py`.
3. Run the script with the desired dataset.

### Example

```python
# Import the function
from utf8_validation import validUTF8

# Sample data
data = [65]

# Validate UTF-8
print(validUTF8(data))  # Output: True
```

## How It Works

### UTF-8 Encoding Rules

- A character in UTF-8 can be 1 to 4 bytes long.
- The number of leading 1s in the first byte determines the number of bytes for the character.
  - 1-byte character: `0xxxxxxx`
  - 2-byte character: `110xxxxx 10xxxxxx`
  - 3-byte character: `1110xxxx 10xxxxxx 10xxxxxx`
  - 4-byte character: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`
- Continuation bytes must start with `10`.

### Algorithm

1. Iterate through each byte in the dataset.
2. Determine the number of bytes in the current UTF-8 character by counting the leading 1s in the first byte.
3. Validate that each subsequent byte in the character starts with `10`.
4. If any byte does not conform to the UTF-8 encoding rules, return `False`.
5. If all bytes are valid, return `True`.

### Code Example

```python
def validUTF8(data):
    n_bytes = 0

    mask_msb = 1 << 7  # 10000000
    mask_msb2 = 1 << 6 # 01000000

    for num in data:
        mask = 1 << 7

        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask >>= 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False

        else:
            if not (num & mask_msb and not(num & mask_msb2)):
                return False

        n_bytes -= 1

    return n_bytes == 0

# Test the function
data = [65]
print(validUTF8(data))  # Output: True
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- Your Name (you@example.com)
```

### Notes
- Replace "Your Name" and "you@example.com" with your actual name and email address.
- Ensure the `LICENSE` file is included in your repository if you reference it in the README.

This `README.md` file provides a comprehensive overview of the project, including how to use it, the underlying logic, and the source code for reference.