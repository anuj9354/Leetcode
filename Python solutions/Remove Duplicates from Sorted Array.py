def removeDuplicates(nums) -> int:
    length , i = len(nums) , 0
    if length:
        j = 0
        while j < length:
            if(nums[j] != nums[i]):
                i+=1
                nums[i] = nums[j]
            j+=1
        i+=1
    
    return i

arr = [int(x) for x in input().split()]
print (removeDuplicates(arr))
