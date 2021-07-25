class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:

    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def remove_date(self, removeData):
        curr = self.headval
        prev = None
        # chak order fris
        if curr.dataval == removeData:
            self.headval = curr.nextval
            curr.nextval = None
        # remove order
        while curr.nextval is not None:

            if curr.dataval == removeData:
                prev.nextval = curr.nextval
                curr.nextval = None
            else:
                prev = curr
                curr = curr.nextval
                # chak order last
                if curr.nextval == None:
                    prev.nextval = None

    def insert_dataHeader(self, dataInsert):
        NewNode = Node(dataInsert)
        head = self.headval
        self.headval = NewNode
        NewNode.nextval = head

    def insert_datalast(self, dataInsert):
        Newnode = Node(dataInsert)
        curr = self.headval
        while True:
            curr = curr.nextval
            if curr.nextval is None:
                curr.nextval = Newnode
                return

    def insert_dataBetween(self, middle_node, datainsert):
        if middle_node == None:
            print("The mentioned node is absent")
            return
        Newnode = Node(datainsert)

        Newnode.nextval = middle_node.nextval
        middle_node.nextval = Newnode


if __name__ == '__main__':

    list = SLinkedList()

    list.headval = Node(1)

    item2 = Node(2)
    list.headval.nextval = item2
    item3 = Node(3)
    item2.nextval = item3
    item4 = Node(4)
    item3.nextval = item4

    # list.remove_date(4)
    list.insert_dataHeader(0)
    list.insert_datalast(5)
    list.insert_dataBetween(item2, 2.1)
    list.listprint()
