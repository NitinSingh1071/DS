class Node:
    def __init__(self, data,next = None):
        self.data = data
        self.next = None

class Linked_list():
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head 
        while(temp): 
            print(temp.data,end=" ") 
            temp = temp.next

    def insertion(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
        if current_node:
            prev.next = current_node.next
            current_node = None
            return
        else:
            return

    def length(self):
        current_node = self.head
        count = 0
        while current_node:
            current_node = current_node.next
            count += 1
        return count

    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None):
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev

    def search_list(self, data):
        count = 0
        pointer = self.head
        while pointer:
            if pointer.data == data:
                count += 1
            pointer = pointer.next
        print(f"\nNumber {data} is present in the list")
        return count

def mergeLists(List_1, List_2):
        head_ptr = temp_ptr = Node(List_1)
        while List_1 or List_2:
            if List_1 and (not List_2 or List_1.data <= List_2.data):
                temp_ptr.next = Node(List_1.data)
                List_1 = List_1.next
            else:
                temp_ptr.next = Node(List_2.data)
                List_2 = List_2.next
            temp_ptr = temp_ptr.next
        return head_ptr.next

D_list = Linked_list()
D_list1 = Linked_list()
D_list.insertion(6)
D_list.insertion(45)
D_list.insertion(30)
D_list1.insertion(41)
D_list1.insertion(88)
D_list1.insertion(32)
print("Linked List : ")
D_list.printList()
D_list.search_list(45)
D_list.delete_node(88)
print("After deleting : ")
D_list.printList()
print("\nReversing the list : ")
D_list.reverse()
D_list.printList()
print("\nMerging two linked list : ")
D_list2 = Linked_list()
D_list2.head = mergeLists(D_list.head, D_list1.head)
D_list2.printList()
