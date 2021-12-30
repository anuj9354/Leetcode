class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    count, ans = 0, ListNode(None)
    y = ans

    while l1 and l2:
        x = count + l1.val + l2.val
        ans.next = ListNode(x % 10)
        count , l1 , l2 , ans = x // 10 , l1.next , l2.next , ans.next

    while l1:
        x = count + l1.val
        ans.next = ListNode(x % 10)
        count , l1 , ans = x // 10 , l1.next , ans.next

    while l2:
        x = count + l2.val
        ans.next = ListNode(x % 10)
        count , l2 , ans = x // 10 , l2.next , ans.next

    if count:
        ans.next = ListNode(count)
        ans = ans.next

    return y.next

a , b = map(int , input().split())
n1 , n2 = ListNode(None) , ListNode(None)
num1 , num2 = n1 , n2

while a:
    n1.next = ListNode(a % 10)
    a , n1 = a // 10 , n1.next

while b:
    n2.next = ListNode(b % 10)
    b , n2 = b // 10 , n2.next

ans1 = addTwoNumbers(num1.next , num2.next)
arr = []
while ans1:
    arr.append(ans1.val)
    ans1 = ans1.next
    
print (arr)

    
