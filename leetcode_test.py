# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 2:54 PM 
# @Author  : Yong Cao
# @Email   : yongcao@fuzhi.ai
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 1
        if 0 in nums:
            return 0
        else:
            for item in nums:
                ret *= item
        return 1 if ret > 0 else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.arraySign([-1,1,-1,1,-1]))