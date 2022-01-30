def twoSum(nums , i: int , res , length: int):
    hashMap , j = {} , i + 1
    while j < length:
        complement = -nums[i] - nums[j]
        if complement in hashMap:
            res.append([nums[i] , nums[j], complement])
            while j+1 < length and nums[j] == nums[j+1]:
                j+=1
        hashMap[nums[j]] = j
        j+=1
    
    return res

def threeSum(nums):
    res, l = [] , len(nums)
    nums.sort()
    for i in range(l):
        if nums[i]>0:
            break
        if i==0 or nums[i-1] != nums[i]:
            twoSum(nums, i ,res, l)
    return res

arr = [int(x) for x in input().split()]
print (threeSum(arr))
        
        
