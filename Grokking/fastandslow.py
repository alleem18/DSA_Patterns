### LinkedList

class Listnode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


def rarrange(head):
    if not head:
        return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next


    prev = None
    while slow :
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # 1->2->3->4->5->6->7->Null

    # 1->2->3
    # 7->6->-5->4->Null

    l = head
    r = prev

    while l and r:
        temp = l.next
        l.next = r
        l = temp

        temp = r.next
        r.next = l
        r = temp

    if l is not None:
        l.next = None
    return head

def detectCycle(head):
    slow = fast = head
    pos1 = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return None
    pos2 = slow
    val = 0
    while pos1 != pos2:
        pos1 = pos1.next
        pos2 = pos2.next
        val+=1

    return val


head = Listnode(1)
node2 = head.next = Listnode(2)
node3 = node2.next = Listnode(3)
node4 = node3.next = Listnode(4)
node5 = node4.next = Listnode(5)
node5.next = node2


res = detectCycle(head)

print(res)

