'''Two Sum'''

from typing import List

print("Two Sum")

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''hash map'''

        dic = dict()
        
        for indx_x, x in enumerate(nums):
            
            target_val = target - x
            # print(dic.get(target_val))
            if dic.get(target_val) != None:
                print([indx_x, dic[target_val]])
                return [indx_x, dic[target_val]]

            else:
                dic[x] = indx_x

        '''Brute Force'''
#         for indx_x, x in enumerate(nums):
            
#             for indx_y, y in enumerate(nums):
                
#                 val = x + y
                
#                 if(val==target and indx_x!=indx_y):
#                     print([indx_x,indx_y])
#                     return [indx_x,indx_y]
                
                

sol = Solution()

sol.twoSum([2,7,11,15], target = 9)
sol.twoSum(nums = [3,2,4], target = 6)
sol.twoSum(nums = [3,3], target = 6)
sol.twoSum(nums = [3,2,3], target = 6)
