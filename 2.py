#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        count = 0
        
        list1 = []
        list2 = []
        
        dummy = ListNode(0)
        dummy.next = l1
        
        while l1:
            count += 1
            
            var = dummy.next
            if dummy.next.next != None:
                dummy.next = dummy.next.next
            
            list1.append(str(var.val))
            print(var)
            
            if var.next == None:
                list1.reverse()
                break
     
        print(f"list 1 = {list1}")
        
        dummy.next = l2
        
        while l2:
            count += 1
            
            var = dummy.next
            if dummy.next.next != None:
                dummy.next = dummy.next.next
            
            list2.append(str(var.val))
            print(var)
            
            if var.next == None:
                list2.reverse()
                break
     
        print(f"list 2 = {list2}")
        
        num = ""
        num2 = ""
        
        for x in list1:
            num += x
            
        for y in list2:
            num2 += y
            
            
            
        print(num)
        print(num2)
        
        num = int(num)
        num2 = int(num2)
        
        result = num + num2
        
        print(result)
        
        result = str(result)
        
        
        dummy = None
        
        for x in result:
            dummy = ListNode(val=x,next=dummy)
            
        print(dummy.val)
        print(dummy.next)
        
        return dummy
        
        
        