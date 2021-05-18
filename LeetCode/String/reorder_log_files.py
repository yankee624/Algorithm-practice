from typing import *
from functools import cmp_to_key

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for log in logs:
            log_split = log.split()
            if log_split[1].isalpha(): letter_logs.append(log)
            else: digit_logs.append(log)
        letter_logs.sort(key=lambda x: [x.split()[1:], x.split()[0]])
        return letter_logs + digit_logs

    # Naive solution
    # def reorderLogFiles(self, logs: List[str]) -> List[str]:
    #     logs.sort(key=cmp_to_key(self.compare_log))
    #     return logs
    #
    # @staticmethod
    # def compare_log(log1: str, log2: str) -> int:
    #     log1_split_idx = log1.find(" ")
    #     log2_split_idx = log2.find(" ")
    #
    #     log1_id = log1[:log1_split_idx]
    #     log2_id = log2[:log2_split_idx]
    #     log1_content = log1[log1_split_idx + 1:]
    #     log2_content = log2[log2_split_idx + 1:]
    #     if log1_content[0].isalpha() and log2_content[0].isalpha():
    #         if log1_content < log2_content:
    #             return -1
    #         elif log1_content > log2_content:
    #             return 1
    #         else:
    #             if log1_id < log2_id:
    #                 return -1
    #             elif log2_id > log2_id:
    #                 return 1
    #             else:
    #                 return 0
    #     elif log1_content[0].isalpha():
    #         return -1
    #     elif log2_content[0].isalpha():
    #         return 1
    #     else:
    #         return 0



s = Solution()
print(s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))