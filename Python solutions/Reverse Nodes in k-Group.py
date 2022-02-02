class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return self.reverseKGroup_Iterative(head, k)
    
    def reverseKGroup_Array(self, head: ListNode, k: int) -> ListNode:
        arr , ans = [] , [] 
        while head:
            arr.append(head.val)
            head = head.next
        
        l1 , i = len(arr), 0
        l2 = l1 - l1%k
        while i < l2:
            j = i + k - 1
            while j >= i:
                ans.append(arr[j])
                j-=1    
            i+=k

        while i < l1:
            ans.append(arr[i])
            i+=1    

        res = point = ListNode(0)
        for x in ans:
            res.next = ListNode(x)
            res = res.next
            
        return point.next
    
    def reverseKGroup_Iterative(self, head: ListNode, k: int) -> ListNode:
        ptr , tail , new_head = head , None , None
        while ptr:
            count , ptr =  0 , head
            while count < k and ptr:
                ptr , count = ptr.next , count + 1
            
            if count == k:
                reverseHead = self.__reverseLinkedList(head , k)
                
                if not new_head: new_head = reverseHead
                elif tail: tail.next = reverseHead
                    
                tail = head
                head = ptr

        if tail: tail.next = head 
            
        if new_head:
            return new_head
        
        return head
    
    def reverseKGroup_Recursive(self, head: ListNode, k: int) -> ListNode:
        count , ptr = 0 , head
        while count < k and ptr:
            ptr , count = ptr.next , count + 1
        
        if count == k:
            reversedHead = self.__reverseLinkedList(head , k)
            head.next = self.reverseKGroup_Recursive(ptr , k)
            
            return reversedHead
        
        return head    
        
    def __reverseLinkedList(self,head: ListNode, k: int) -> ListNode:
        new_head , ptr = None, head
        while k:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr , k = next_node , k - 1
        
        return new_head

arr = [int(x) for x in input().split()]
k = int(input())
head = point = ListNode(0)
for x in arr:
    head.next = ListNode(x)
    head = head.next

sol = Solution()
ans , ansArr = sol.reverseKGroup(point.next , k) , []
while ans:
    ansArr.append(ans.val)
    ans = ans.next

print (ansArr)
