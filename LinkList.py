# Programmer -- SHIVAJI DAS
# Date -- 28 December 2023
# Description -- This file Contains 8 functions on SinglyLinkList implemented by SHIVAJI DAS

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        if self.head == None:
            print('List is empty')
            return
        
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
         

    def InsertAtBeg(self,value):
        # Creating a new Node
        new_node = Node(value)
        
        #Inserting new Node at the beginning
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def InsertAtEnd(self,value):
        #Creating a new Node
        new_node = Node(value)
        
        # Inserting at the end if LL is empty or Insering at the end 
        # with traversing still last node
        if self.head is None:
           self.head = new_node
        else:   
            temp = self.head
            while temp.next is not None:
                temp = temp.next  

            temp.next = new_node   
        self.length += 1 


    def InsertAtPos(self,value,index):
        # If the list is empty we are ignoring the index and creating a LL by adding it
        # at the end using InsertAtEnd() function we can also directly handle it here
        if self.length == 0:
            self.InsertAtEnd(value)
            return

        # Doing Index Validation
        if index < 1 or index > (self.length + 1):
            print("Invalid Index")
            return
        # Creating a new node
        new_node = Node(value)
        
        # Inserting Node at specific index Position first for if index is 1
        # Then for last index and then in middle elements of LL
        if index == 1: 
            new_node.next = self.head
            self.head = new_node
        elif index == (self.length + 1): 
            if self.head is None:
               self.head = new_node
            else:   
               temp = self.head
               while temp.next is not None:
                   temp = temp.next  
               temp.next = new_node 
        else:
            temp = self.head
            for _ in range(1,index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1     


    def DeleteAtBeg(self):
        # Validating if List is empty or not
        if self.head == None:
            print("List is Already Empty")
            return
        
        # If only one list or more then one list we are deleting
        if self.length == 1:
            self.head = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length  -= 1  


    def DeleteAtEnd(self):
        # Validating if List is empty or not
        if self.head == None:
            print("List is Already Empty")
            return
        
        # If only one list or more then one list we are deleting
        if self.length == 1:
            self.head = None 
        else:
            temp = self.head
            # for _ in range(1,self.length - 1):
            #     temp = temp.next
            # temp.next = None
            # or
            while(temp.next.next is not None):
                temp = temp.next
            temp.next = None    
        self.length -= 1      


    def DeleteAtPos(self,index):
        # Validating if List is empty or not
        if self.head is None:
            print('List is Empty')
            return
        
        # Doing Index Validation
        if index < 1 or index > self.length:
            print('Invalid Index')
            return

        # Deleteing Node at first,last and At middle according to the
        # input from the user
        if index == 1:
            temp = self.head
            self.head = self.head.next
            temp = None
        elif index == self.length:
            if self.length == 1:
                self.head = None
            else:
                temp = self.head
                for _ in range(1,index-1):
                    temp = temp.next
                temp.next = None
        else:
            temp = self.head
            # for _ in range(1,index-1):
            #     temp = temp.next
            i = 1
            while(i < index-1):
                temp = temp.next
                i= i+1
            delNode = temp.next
            temp.next = temp.next.next
            delNode = None

        self.length-= 1                               

   
    def ListCount(self):
        return self.length    

SinglyLL = LinkList()
choice = -1

while(choice != 0):
    print('1 : InsertAtBeg')
    print('2 : InsertAtEnd')
    print('3 : InsertAtPos')
    print('4 : PrintList')
    print('5 : CountList')
    print('6 : DeleteFirst')
    print('7 : DeleteLast')
    print('8 : DeleteAtPos')
    print('0 : Type Zero To Exit')
    choice = int(input("Enter The Choice"))
    match choice:
        case 1:
            value = int(input())
            SinglyLL.InsertAtBeg(value)
        case 2:
            value = int(input())
            SinglyLL.InsertAtEnd(value)
        case 3:
            value = int(input())
            print('Enter The Positions')
            pos = int(input())
            SinglyLL.InsertAtPos(value,pos)
        case 4:
            print(SinglyLL)
        case 5:
            SinglyLL.ListCount() 
        case 6:
            SinglyLL.DeleteAtBeg()
        case 7:
            SinglyLL.DeleteAtEnd()
        case 8:
            pos = int(input('Enter The position To Delete'))
            SinglyLL.DeleteAtPos(pos)               
        case 0:
            choice = 0
        case _:
            print('Wrong Choice')                


