class Node:
    def __init__(self, dataVal = None):
        self.dataVal = dataVal
        self.nextNode = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printLinkedList(self):
        if self.head is None:
            print("The Linked-List is empty . Please add some nodes ;)\n")
        else:
            next = self.head
            print("\nElements of Linked-List Are:",end=' ')
            while next is not None:
                print(next.dataVal,end=' ')
                next = next.nextNode
            print("\n")

    def reverseLinkedlist(self,prev,cur):
        if cur :
            self.reverseLinkedlist(cur,cur.nextNode)
            cur.nextNode = prev
        else:
            self.head = prev
            print("\nThe Linked-List has been reversed")

    def printSuccessAdd(self,data):
        print("\nNode with data \"{}\" has been added successfully\n".format(data))

    def printSuccessDel(self,data):
        print("\nNode with data \"{}\" has been deleted successfully\n".format(data))

    def addNodeAtBeginning(self):
        data = input("\nEnter Data to be inserted as Node:\n")
        node = Node(data)
        node.nextNode = self.head
        self.head = node
        self.printSuccessAdd(data)

    def addNodeAtEnd(self):
        if self.head is None:
            choice= input("\nThere are no elements in the linked-list . Do you still want to add ? y for yes /any key to exit\n")
            if(choice.lower()=='y'):
                data = input("\nEnter Data to be inserted as Node:\n")
                node = Node(data)
                node.nextNode = self.head
                self.head = node
                self.printSuccessAdd(data)
                return
            else:
                return
        else :
            data = input("\nEnter Data to be inserted as Node:\n")
            node = Node(data)
            next = self.head
            while next.nextNode is not None:
                next = next.nextNode
            next.nextNode = node
            self.printSuccessAdd(data)

    def addNodeAfter(self):

        data = input("\nEnter Data to be inserted as Node.\n")
        dataA = input("\nEnter Data after which the Node is to be inserted:\n")
        node = Node(data)
        next = self.head
        while (next.dataVal != dataA):
            next = next.nextNode
            if next is None :
                print("\nThe given data is not present at any node. Please try again.\n")
                return

        if next.nextNode is None:
            choice=input("\nThe given data is at the end. Do you want to continue ? y for yes/any key to exit\n")
            if choice.lower()=='y':
                next.nextNode = node
                self.printSuccessAdd(data)
            else:
                return
        else:
            node.nextNode = next.nextNode
            next.nextNode = node
            self.printSuccessAdd(data)

    def addNodeBefore(self):

        data = input("\nEnter Data to be inserted as Node:\n")
        dataB = input("Enter Data before which the Node is to be inserted:\n")
        node = Node(data)
        cur = self.head
        if cur.nextNode is None or cur.dataVal == dataB:
            if(cur.dataVal != dataB):
                print("The given data is not present at any node. Please try again.\n")
                return
            else:
                node.nextNode = cur
                self.head = node
                self.printSuccessAdd(data)
                return

        while cur.nextNode.dataVal !=dataB:
            cur = cur.nextNode
            if cur.nextNode is None:
                print("\nThe given data is not present at any node. Please try again.\n")
                return
        node.nextNode = cur.nextNode
        cur.nextNode = node
        self.printSuccessAdd(data)

    def deleteNodeAtBeginning(self):

        data = self.head.dataVal
        self.head = self.head.nextNode
        self.printSuccessDel(data)


    def deleteNodeAtEnd(self):

        next = self.head
        if next.nextNode is None :
            choice = input("\nThere is only one element present in the list. Do you want to continue ? y for yes/any key to exit\n")
            if choice.lower() == 'y':
                data = self.head.dataVal
                self.head = None
                self.printSuccessDel(data)
            else:
                return
        else:
            while next.nextNode.nextNode is not None:
                next = next.nextNode
            data = next.nextNode.dataVal
            next.nextNode = None
            self.printSuccessDel(data)

    def deleteSpecificNode(self):

        data = input("\nEnter Data to be deleted:\n")
        next = self.head
        if next.dataVal == data :           #if the data is present at beginning only
            self.deleteNodeAtBeginning()
            return
        if next.nextNode is None :
            if next.dataVal == data:
                self.head = None
                self.printSuccessDel(data)
            else:
                print("Sorry ! The given data is not present in the list")
                return
        elif next.nextNode.nextNode is None:
            if next.nextNode.dataVal == data:
                next.nextNode = None
                self.printSuccessDel(data)
            else:
                print("Sorry ! The given data is not present in the list")
                return
        else:
            while next.nextNode.dataVal != data:
                next = next.nextNode
                if next.nextNode is None:
                    print("Sorry ! The given data is not present in the list")
                    return
            next.nextNode = next.nextNode.nextNode
            self.printSuccessDel(data)






