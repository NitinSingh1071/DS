class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self,data):
       if self.val:
           if data < self.val:
               if self.left is None:
                   self.left = Node(data)
               else:
                    self.left.insert(data)
           elif data>self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
       else :
            self.val = data

    def PrintTree(self):
        if  self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()


    def printPreorder(self):
        if self.val:
            print(self.val)
            if self.left:
                self.left.printPreorder()
            if self.right:
                self.right.printPreorder()
                
    
    
    def  printInorder(self):
        if self.val :
            if self.left:
                self.left.printInorder()
            print(self.val)
            if self.right:
                self.right.printInorder()

    def printPostorder(self):
        if self.val:
            if self.left:
                self.left.printPostorder()
            if self.right:
                self.right.printPostorder()
            print(self.val)


root = Node(59)
root.left = Node(7)
root.right = Node(98)
root.left.right = Node(15)
root.left.right.right = Node(38)
root.right.right = Node(110)

root.PrintTree()

print('ordering with insert and printing' )
root1 = Node(59)
root1.insert(7)
root1.insert(15)
root1.insert(38)
root1.insert(98)
root1.insert(110)
root1.PrintTree()

print("Inorder")
root1.printInorder()

print("Preorder")
root1.printPreorder()

print("Postorder")
root1.printPostorder()

        
