# # write a solution with O(n) time complexity
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             if target-nums[i] in nums:
#                 return [i,nums.index(target-nums[i])]

# # time complexity: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # donot give me hint now
        # # 1. brute force
        for i in nums:          
            if target-i in nums:
                return nums.index(i),nums.index(target-i)



# main
if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums,target))