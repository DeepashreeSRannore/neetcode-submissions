

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        hashmap = {None:None}

        cur=head
        while cur:
            copy=Node(cur.val)
            hashmap[cur] = copy
            cur=cur.next
        
        cur=head
        while cur:
            copy=hashmap[cur]
            copy.next=hashmap[cur.next]
            copy.random=hashmap[cur.random]
            cur=cur.next
        
        return hashmap[head]


        