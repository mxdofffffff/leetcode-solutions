head = [1,2,3,4,5]
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev

        prev = current
        current = next_node
    return prev
print(reverse_list(head))