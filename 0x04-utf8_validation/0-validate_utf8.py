#!/usr/bin/python3
"""
This module defines the validUTF8 function.
"""


def validUTF8(data):
    """Check if a list of integers represents a valid UTF-8 encoding."""
    num_bytes = 0  # Number of bytes remaining in the current UTF-8 character

    for num in data:
        # Mask to extract the first 8 bits of each integer
        num &= 0xFF

        if num_bytes == 0:
            # Check how many bytes this character requires
            if (num >> 5) == 0b110:      # 2-byte character
                num_bytes = 1
            elif (num >> 4) == 0b1110:   # 3-byte character
                num_bytes = 2
            elif (num >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (num >> 7):             # Invalid 1-byte character
                return False
        else:
            # Check that the next byte starts with "10"
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

    # All characters must be completely processed (num_bytes should be 0)
    return num_bytes == 0
