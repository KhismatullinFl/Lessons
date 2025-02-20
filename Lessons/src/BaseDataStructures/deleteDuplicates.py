class Solution(object):
    def deleteDuplicates(self, head):
        cur = head
        while(cur.next.next):
            if(cur.val==cur.next.val):
                cur.next = cur.next.next
            else:
                cur = cur.next
