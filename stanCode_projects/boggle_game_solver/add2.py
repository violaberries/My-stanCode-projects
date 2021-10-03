"""
File: add2.py
Name:
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    h1, h2, prev = l1, l2, None
    carry = 0
    while h1 != None and h2 != None:
        sm = h1.val + h2.val + carry
        carry = sm // 10
        h1.val = sm % 10
        prev = h1
        h1 = h1.next
        h2 = h2.next

    if h2 != None:
        h1 = h2
        # since we are overriding the first linked list, so our priority is on head1
        if prev != None:
            # if case will handle this edge case l1 = [] l2 = [1,2,3]
            prev.next = h2

    while h1 != None:
        sm = h1.val + carry
        carry = sm // 10
        h1.val = sm % 10
        prev = h1
        h1 = h1.next
    if carry:
        prev.next = ListNode(carry)
    return l1


    # result = ListNode(0)
    # result_tail = result
    # carry = 0
    #
    # while l1 or l2 or carry:
    #     val1 = (l1.val if l1 else 0)
    #     val2 = (l2.val if l2 else 0)
    #     carry, out = divmod(val1 + val2 + carry, 10)
    #
    #     result_tail.next = ListNode(out)
    #     result_tail = result_tail.next
    #
    #     l1 = (l1.next if l1 else None)
    #     l2 = (l2.next if l2 else None)
    #
    # return result.next


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
