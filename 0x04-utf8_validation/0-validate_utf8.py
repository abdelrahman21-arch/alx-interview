#!/usr/bin/python3
"""
utf8 - validation
"""

def validUTF8(data):
    """

    Args:
        data: data o be validated

    Returns: true if the data is utf8 else not true

    """
    # define the number of bytes
    n_bytes = 0

    # creating a mask to read the n bits
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

