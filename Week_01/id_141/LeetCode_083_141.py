class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next

        return head
def main():
    a = ListNode(1)
    a.next = ListNode(1)
    a.next.next = ListNode(2)

    s1 = Solution()
    print(s1.deleteDuplicates(a))

if __name__ == '__main__':
    main()
