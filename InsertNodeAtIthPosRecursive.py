# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 22:17:18 2025

@author: Acer
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
def takeinputoptimized():
    input_list =[int(ele) for ele in input("Enter elements of linked list, end with -1\n").split()]
    head=None
    tail=None
    for currele in input_list:
        if currele==-1:
            break
        newNode=Node(currele)
        if head is None:
            head=newNode
            tail=head
        else:
            tail.next=newNode
            tail=newNode
        
    return head

def printLL(head):
    while head is not None:
        if head.next is None:
            print(head.data)
        else:
            print(head.data,end="->")
        head=head.next
        
def lengthLL(head):
    node_count=0
    while head is not None:
        if head.data==-1:
            break
        node_count=node_count+1
        head=head.next
    return node_count

def printIthNode(head,i):
    count=0
    while head is not None:
        if count==i:
            #print(head.data)
            break
        count+=1
        head=head.next
        
    return head.data


def InsertNodeAtLastPosition(node,head):
    prevptr=head
    while prevptr.next is not None:
        prevptr=prevptr.next
    prevptr.next=node
    printLL(head)
    
def InsertNodeAtIthPosition(node,head,pos):
    if pos>lengthLL(head)+1:
        return -1
    else:
        if head is None:
            head=node
        elif pos ==1:
            node.next=head
            head=node
        else:
            prevptr=None
            currptr=head
            count=1
            while currptr is not None:
                if count==pos:
                    break
                prevptr=currptr
                currptr=currptr.next
                count=count+1
            prevptr.next=node
            node.next=currptr
        printLL(head)
    return 1
    

def deleteNodeAtIthPosition(head,pos):
    print("\nLinked-List beforoe deletion")
    printLL(head)   
    if head is None:
        print("Empty Linked List")
    
    elif pos>lengthLL(head):
        print("\nCan't delete at mentioned position")
    elif pos==0:
        ptr=head
        head=head.next
        ptr.next=None
    else:
        prevptr=None
        ptr=head
        count=0
        
        while count<pos:
            prevptr=ptr
            ptr=ptr.next
            count=count+1
        
        prevptr.next=ptr.next
        ptr.next=None
    print("\nLinked-List after deletion")
    printLL(head)
    return head

    
def InsertNodeAtIthPosRecursive(node,head,i):
    if head is None:
        nide=head
        return node
        return node
    if i<0 or i>lengthLL(head)+1:
        return head
    if i==0:
        node.next = head
        return node
    
    smallhead = InsertNodeAtIthPosRecursive(node,head.next,i-1)
    head.next=smallhead
    return head
        

pos=3
head = takeinputoptimized()
node=Node(10000)
head = InsertNodeAtIthPosRecursive(node,head,pos)
printLL(head)
# x = InsertNodeAtIthPosition(node,head,pos)
# if x==-1:
#     print("Error: Enter the position within the length of the linked list")
# else:
#     print("Success")