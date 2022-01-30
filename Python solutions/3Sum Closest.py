def twoSum(nums , target: int , i: int , l: int , ans: int):
    x , y = i + 1 , l
    while x < y:
        z = nums[i] + nums[x] + nums[y]
        if z < target:
            x+=1
        elif z > target:
            y-=1
        else:
            return target
        if abs(target - z) < abs(target - ans):
            ans = z
    return ans
            
class Solution:
    def threeSumClosest(self , nums , target: int) -> int:
        ans , i , l = -10000000 , 0 , len(nums) - 1
        nums.sort()
        while i<=l and ans != target:
            if i==0 or nums[i] != nums[i-1]: 
                ans = twoSum(nums, target, i , l , ans)
            i+=1
        return ans

arr = [int(x) for x in input().split()]
target = int(input())
sol = Solution()

print (sol.threeSumClosest(arr, target))
