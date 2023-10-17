class LinkedList:
    def __init__(self,data):
        self.start=None
        self.temp=None
    def create_list(self):
        for i in range(10):
            new_node=LinkedList(i)
            if self.start is None:
                self.start=new_node
                self.temp=self.start
            else:
                self.temp.next=new_node
                self.temp=self.temp.next
        return self.start
    def print_list(self):
        while self.start.next:
            print(self.start.data,end=" ")
            self.start=self.start.next
            print()

    def  length(self):
        temp=self.start
        count=0
        while(temp!=None):
            temp=temp.next
            count=count+1
        return count
    def find_median(self):
        self.temp=self.start
        length=self.find_length()
        counter=length//2
        counter=counter-1
        i=0
        while i!=counter and self.temp is not None:
            self.temp=self.temp.next
            i=i+1
        if length %2==1:
            return self.temp.next.data


object=LinkedList()
start=object.LinkedList()
object.create_list()
length=object.length()
print(length)
median=object.find_median()
object.print_list()

