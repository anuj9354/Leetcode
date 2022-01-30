from queue import PriorityQueue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeKLists_divide_conquer(lists)
    
    # Merge One by One [O(k*N)] where N is total number of nodes.
    def mergeKLists_1_by_1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans , k = ListNode(0) , len(lists)
        done, ans2 = [False] * k , ans
        while k:
            i , check, pos , mini = 0 , False, 0 , 1000000
            while i < k:
                if not done[i]:
                    check = True
                    if lists[i] and lists[i].val < mini:
                        pos , mini = i , lists[i].val
                i += 1
            
            if not lists[pos]:
                done[pos] = True
                
            if done[pos]:
                break
                              
            ans.next = ListNode(lists[pos].val)
            ans , lists[pos] = ans.next , lists[pos].next  
        
        return ans2.next
    
    # Merge One by One [O(k*N)] where N is total number of nodes.
    def mergeKLists_1_by_1_PQ(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = point = ListNode(0)
        q = PriorityQueue()
        
        for x in lists:
            while x:
                q.put((x.val))
                x = x.next
        
        size = q.qsize()
        for i in range(size):
            point.next = ListNode(q.get())
            point = point.next
                           
        return head.next

    def mergeKLists_Arrays(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = head = ListNode(0)
        arr = []
        
        for x in lists:
            while x:
                arr.append(x.val)
                x = x.next
        
        arr.sort()
        for x in arr:
            head.next = ListNode(x)
            head = head.next
            
        return ans.next 
    
    def mergeKLists_divide_conquer(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        count = len(lists)   
        if count :
            interval = 1
            while interval < count:
                i , z = 0 , interval * 2
                for i in range (0 , count - interval , z):
                    lists[i] = self.__merge2Lists(lists[i] , lists[i + interval])    
                interval = z
            
            return lists[0]
        
        return None
    
    def __merge2Lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = point = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = ListNode(l1.val)
                l1 = l1.next
            else:
                point.next = ListNode(l2.val)
                l2 = l2.next
            point = point.next
        
        if not l1:
            point.next = l2
        else:
            point.next = l1
        
        return head.next 
