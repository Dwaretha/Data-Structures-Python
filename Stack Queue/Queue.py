class queue:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop(0)
    def display(self):
        print( self.items)
s=queue()
print("1.enqueue\n2.dequeue\n3.display\nEnter your choice")
n=int(input())
if(n==1):
    x=input("Enter the item to enqueue")
    s.enqueue(x)
    s.display()
elif(n==2):
    if s.isempty():
        print("The queue is empty")
    else:
        print("poped value",s.dequeue())
    s.display()
elif n==3:
    if s.isempty():
        print("The queue is empty")
    else:
        print("the queue contains",s.display())
else:
    print("Invalid option")
