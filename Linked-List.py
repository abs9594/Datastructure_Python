import index

def addNode(linkedList):
    listOfFunc = {'1': 'linkedList.printLinkedList()', '2': 'linkedList.addNodeAtBeginning()',
                  '3': 'linkedList.addNodeAtEnd()', '4': 'linkedList.addNodeAfter()', '5': 'linkedList.addNodeBefore()',
                  '6': 'return'}
    while 1:
        choice = input("Enter Choice for action on Linked-List:\n\n "
                       "1.Print Linked-List\n 2.Add Node At Beginning\n "
                       "3.Add Node At End\n 4.Add Node After\n "
                       "5.Add Node Before\n 6.Return to Main Menu\n")
        if choice not in ['1','2','3','4','5','6']:
            print("Choice number is not valid .Please Enter Valid Choice\n")
            continue
        else:
            if choice=='6':
                return
            elif choice == '2' or '3':
                eval(listOfFunc[choice])
            else:
                if linkedList.head is None :
                    print("The Linked-List is empty . Please add some nodes ;)\n")
                else:
                    eval(listOfFunc[choice])

def deleteNode(linkedList):
    listOfFunc = {'1': 'linkedList.printLinkedList()','2': 'linkedList.deleteNodeAtBeginning()', '3': 'linkedList.deleteNodeAtEnd()',
                  '4': 'linkedList.deleteSpecificNode()', '5': 'return'}
    while 1:
        choice = input("Enter Choice for action on Linked-List:\n\n "
                       "1.Print Linked-List\n 2.Delete Node At Beginning\n "
                       "3.Delete Node At End\n 4.Delete Node with specific data\n "
                       "5.Return to Main Menu\n")
        if choice not in ['1','2','3','4','5']:
            print("Choice number is not valid .Please Enter Valid Choice\n")
            continue
        else:
            if choice=='5':
                return
            else:
                if linkedList.head is None :
                    print("The Linked-List is empty . Please add some nodes ;)\n")
                else:
                    exec(listOfFunc[choice])



linkedList = index.LinkedList()
listOfFunc = {'1': 'linkedList.printLinkedList()', '2': 'addNode(linkedList)',
              '3': 'deleteNode(linkedList)','4': 'linkedList.reverseLinkedlist(None,linkedList.head)' , '5': 'exit()'}
try:
    while 1 :

        choice = input("\nWelcome to Linked-List programme\nEnter Choice for action on Linked-List:\n\n "
                       "1.Print Linked-List\n 2.Add a Node\n "
                       "3.Delete a Node\n 4.Reverse the Linked-List\n 5.EXIT\n")

        if choice not in ['1','2','3','4','5']:
            print("Choice number is not valid .Please Enter Valid Choice\n")
            continue

        else:
            exec(listOfFunc[choice])

except Exception as e:
    print(e)




