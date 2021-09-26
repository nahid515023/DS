class Node:
    def __init__(self, data=None, node=None):
        self.data = data
        self.node = node


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            itr = self.head
            while itr.node:
                itr = itr.node
            itr.node = Node(data, None)

    def insert_value(self,list_data):
        self.head=None
        for data in list_data:
            self.insert_at_end(data)
    
    def length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr=itr.node
        return count

    def remove_index(self,index):
        if index<0 or index>self.length():
            raise Exception("Invalid index")
        elif index==0:
            self.head=self.head.node
        else:
            count=0
            itr = self.head
            while itr:
                if count == index-1:
                    itr.node = itr.node.node
                    break
                itr=itr.node
                count+=1

    def insert_index(self,index,data):
        if index<0 or index>self.length():
            raise Exception("Invalid index")
        
        elif index==0:
            self.insert_at_begining(data)

        else:
            count=0
            itr = self.head
            while itr:
                if count == index-1:
                    node=Node(data,itr.node)
                    itr.node = node
                    break
                itr=itr.node
                count+=1
    

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        while itr:
            print(itr.data, end='-->')
            itr = itr.node
        print()


if __name__ == '__main__':
    ll = Linked_list()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(100)
    # ll.insert_at_begining(1000)
    # ll.insert_at_end(2000)
    ll.insert_value([1,2,3,4,5,6,7])
    ll.print()
    ll.remove_index(0)
    ll.print()
    ll.insert_index(0,5000)
    ll.print()
    print(ll.length())
