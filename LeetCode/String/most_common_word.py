from collections import Counter
import re
from typing import *

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        replaced = re.sub("[^a-z\s]", " ", paragraph.lower())
        count = Counter(replaced.split())
        for word in banned:
            count.pop(word, None)
        return count.most_common(1)[0][0]

s = Solution()
print(s.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit","aa"]))