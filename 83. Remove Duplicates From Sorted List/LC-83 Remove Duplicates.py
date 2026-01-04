class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicates(head: ListNode) -> ListNode: 
     
    current = head
    
    while current and current.next:
        
        if current.val == current.next.val:  # Compare values, not nodes
            current.next = current.next.next
            
        else:
            current = current.next
            
    return head
