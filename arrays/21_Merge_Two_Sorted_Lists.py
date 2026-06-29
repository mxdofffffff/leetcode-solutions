list1 = [1,2,4]
list2 = [1,3,4]
def mergeTwoLists(list1,list2):
    dummy = ListNode(-1)
    current = dummy
    while list1 and list2:
        if list1.val<=list2.val:
           current.next = list1.val
           list1.val=list1.next
        else:
            current.next = list2.val
            list2.val = list2.next
        current = current.next

    current.next = list1 or list2
    return dummy.next