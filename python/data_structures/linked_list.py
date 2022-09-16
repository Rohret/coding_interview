
class node():
    def __init__(self,val):
        self.val = val
        self.next = None

class linkedList():
     def __init__(self):
         self.head = None

     def listprint(self):
         printval = self.head
         while printval is not None:
            print(printval.val)
            printval = printval.next

     def append(self,val):
        new_node = node(val)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node


list = linkedList()
list.head = node("Monday")
list.append("Tuesday")
list.append("Wednesday")

# list.head.next = l2
# l2.next = l3

list.listprint()

