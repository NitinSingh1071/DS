class Node:
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None

class Polynomial:
    def __init__(self, degree=None, coefficient=None):
        if degree is None:
            self.polyHead = None
        else:
            self.polyHead = Node(degree, coefficient)
        self.polyTail = self.polyHead

    def degree(self):
        if self.polyHead is None:
            return -1
        else:
            return self.polyHead.degree

    def __add__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0
        newPoly = Polynomial()
        nodeA = self.polyHead
        nodeB = rhsPoly.polyHead

        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                coefficient = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                coefficient = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree
                coefficient = nodeA.coefficient + nodeB.coefficient
                nodeA = nodeA.next
                nodeB = nodeB.next

            newPoly.appendTerm(degree, coefficient)

        while nodeA is not None:
            newPoly.appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        while nodeB is not None:
            newPoly.appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next

        return newPoly

    def appendTerm(self, degree, coefficient):
        if coefficient != 0.0:
            newTerm = Node(degree, coefficient)
            if self.polyHead is None:
                self.polyHead = newTerm
            else:
                self.polyTail.next = newTerm

            self.polyTail = newTerm

    def printPoly(self):
        currentNode = self.polyHead
        while currentNode is not None:
            if currentNode.next is not None:
                print(f"{currentNode.coefficient}x^{currentNode.degree} + ")
            else:
                print(f"{currentNode.coefficient}x^{currentNode.degree}")
            currentNode = currentNode.next

if __name__ == "__main__":
    pol1 = Polynomial(4, 2) 
    pol1 += Polynomial(7, -6)
    pol1 += Polynomial(1, 10)
    print("First Polynomial : ")
    pol1.printPoly()
    pol2 = Polynomial(1, 12)
    pol2 += Polynomial(1, 4)
    pol2 += Polynomial(0,5)
    print("Second Polynomial : ")
    pol2.printPoly()
    addPoly = pol1 + pol2
    print("The addition of the two polynomials is:")
    addPoly.printPoly()
