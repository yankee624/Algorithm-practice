from typing import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start_idx = 0
        curr_idx = 0
        gas_tank = 0 # accumulated gas
        while True:
            if curr_idx == len(gas):
                break
            gas_tank += gas[curr_idx] - cost[curr_idx]
            # if accumulated amount gets negative, start_idx ~ curr_idx cannot be the start of the circuit
            # because if we start in between, we would start from 0 instead of positive amount (-> worse)
            if gas_tank < 0:
                start_idx = curr_idx + 1
                gas_tank = 0
            curr_idx += 1

        return start_idx


s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
