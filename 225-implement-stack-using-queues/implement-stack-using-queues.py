


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
'''
# class / object / constructor/ self / init/ method

    # Defining a class called Automobile
class Automobile:
    
    # Constructor: __init__ method 
    # self -- It allows the object to refer to its own attributes and methods.
    # self -- check access the variables or methods within class
    def __init__(self, make, model, year, color):
        self.make = make        # e.g., Toyota
        self.model = model      # e.g., Corolla
        self.year = year        # e.g., 2021
        self.color = color      # e.g., Red

    # Method: Display car information
    def display_info(self):
        print(f"{self.year} {self.color} {self.make} {self.model}")
    
    # Method: Honk
    def honk(self):
        print(f"{self.make} {self.model} says: Beep beep!")

    # Creating objects (cars) from the Automobile class
    car1 = Automobile("Toyota", "Corolla", 2021, "Red")
    car2 = Automobile("Tesla", "Model S", 2023, "Black")

    # Using methods
    car1.display_info()   # Output: 2021 Red Toyota Corolla
    car1.honk()           # Output: Toyota Corolla says: Beep beep!
'''

class MyStack:

    def __init__(self):

        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:

        self.q1.append(x)

    def pop(self) -> int:

        #print(self.q1) 
        while len(self.q1) > 1:
            #only accessing the option of top or q1[0]
            self.q2.append(self.q1[0])
            self.q1.popleft()

        #print(self.q1)    
        var = self.q1[0]    

        self.q1 = self.q2.copy()

        self.q2.clear()

        return var  
        

    def top(self) -> int:

        print(self.q1) 
        print(self.q2) 
       
        while len(self.q1) > 1:
            # q2 - 1 2 3 4
            #only accessing the option of top or q1[0]
            self.q2.append(self.q1[0])
            self.q1.popleft()

        var = self.q1[0]   
        self.q2.append(self.q1[0]) 
        

        #self.q1 = self.q2 #shallow copy , make a deep copy

        self.q1 = self.q2.copy()

        self.q2.clear() 

        #print("q1 is",self.q1)
        #print("q2 is",self.q2)
 

        return var      


    def empty(self) -> bool:

        return False if self.q1 else True

        


        
        
        # for pop()
        #impliment with queues
        #var -- 4
        #Q1 1 2 3 -- remove  three time to reach end
        #Q2
        # for queue FIFO - append and popleft
        # For stack LIFO - append  and pop
        # shallow copy deep copy

        # 1 2 3 4
        # 1 2 3


        