class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def endinsert(head,data):
    new = Node(data) 
    if head is None:
        return new
    temp=head
    while temp.next:
        temp = temp.next
    temp.next = new
    return head

def printd(head):
    temp=head
    while temp:
        print(temp.data,end=" ")
        temp=temp.next
        
n=int(input())
n= list(map(int, input().split()))

head = None
for num in n:
    head = endinsert(head, num)

printd(head)

pos=int(input())
ele=int(input())

temp=Node(ele)
Node.next=self.head.next
self.head.next=Node
