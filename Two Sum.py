def twoSum_twoPass(nums: List[int], target: int) -> List[int]:
    visited , l = {} , len(nums)

    for i in range(l):
        visited[nums[i]] = i  
    
    for i in range(l):
        x = target - nums[i]
        if x in visited and i != visited[x]:
            return [i, visited[x]]

def twoSum_onePass(nums: List[int], target: int) -> List[int]:
    visited , l = {} , len(nums)
    
    for i in range(l):
        x = target - nums[i]
        if x in visited:
            return [visited[x], i]
        visited[nums[i]] = i       

arr = [int(x) for x in input().split()]
target = int(input())
print (twoSum_onePass(arr, target))
print (twoSum_twoPass(arr, target))
    
