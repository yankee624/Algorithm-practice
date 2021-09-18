from typing import *


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # smallest to largest
        people.sort(key=lambda x: (x[0], -x[1]))
        result = [0] * len(people)

        for p in people:
            order = p[1] # which index p has to go (excluding the already positioned ones)
            idx = 0
            while order > 0 or result[idx] != 0:
                # count only if slot is empty (since we need to exclude already positioned ones)
                if result[idx] == 0:
                    order -= 1
                idx += 1
            result[idx] = p
        return result


s = Solution()
print(s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))