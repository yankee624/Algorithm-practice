from typing import *


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        idx = 0
        while True:
            if idx >= len(data):
                return True
            first_byte = data[idx]
            encoding_length = 0
            if first_byte >> 7 == 0:
                encoding_length = 1
            elif first_byte >> 5 == 0b110:
                encoding_length = 2
            elif first_byte >> 4 == 0b1110:
                encoding_length = 3
            elif first_byte >> 3 == 0b11110:
                encoding_length = 4
            else:
                return False
            for _ in range(encoding_length-1):
                idx += 1
                if idx >= len(data):
                    return False
                byte = data[idx]
                if byte >> 6 != 0b10:
                    return False
            idx += 1


s = Solution()
print(s.validUtf8([197,130,1]))
