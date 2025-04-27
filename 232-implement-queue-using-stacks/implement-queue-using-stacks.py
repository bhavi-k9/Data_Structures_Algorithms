class MyQueue:

    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()
        

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:

        while len(self.s1) > 1:
            # append last element to q2 then pop
            # how to get last element
            self.s2.append(self.s1[-1])
            self.s1.pop()

        var = self.s1[-1]    

        #s1 - 
        #s2 - 432
        #self.s1 = self.s2.copy()

        self.s1.pop() #not in peek

        # push all elements one by one from s2 to s1
        # same as above
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()  #forgot clear s2


        return var  
        
##################################
        

    def peek(self) -> int:

        while len(self.s1) > 1:
            # append last element to q2 then pop
            # how to get last element
            self.s2.append(self.s1[-1])
            self.s1.pop()

        var = self.s1[-1]    

        # push all elements one by one from s2 to s1

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()


        return var  
        
        

    def empty(self) -> bool:

        return False if self.s1 else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


       
        

       
        


       
           
        