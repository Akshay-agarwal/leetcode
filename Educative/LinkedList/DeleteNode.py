class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def deleteNode(head, target):
    curr = head
    prev = ListNode(0)

    while curr:
        if curr.val == target:
            break
        prev = curr
        curr = curr.next

    if curr == head:
        return head.next
    elif curr == None:
        return head
    prev.next = curr.next
    return head
