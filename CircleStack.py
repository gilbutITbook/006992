class Circle(object):
    def __init__(self):
        self.radius = 0
        
    def change_radius(self, radius):
        self.radius = radius
        
    def get_radius(self):
        return self.radius
        
    def __str__(self):
        return "circle: "+str(self.radius)
        
class Stack(object):
    def __init__( self):
        self.stack = []
        
    def get_stack_elements(self):
        return self.stack.copy()
        
    def add_one(self , item):
        self.stack.append(item)
        
    def add_many(self , item, n):
        for i in range(n):
            self.stack.append(item)
            
    def remove_one(self):
        self.stack.pop()
        
    def remove_many(self , n):
        for i in range(n):
            self.stack.pop()
            
    def size(self):
        return len(self.stack)
        
    def prettyprint(self):
        for thing in self.stack[::-1]:
            print('|_',thing, '_|')
            
    def __str__(self):
        ret = ""
        for thing in self.stack[::-1]:
            ret += ('|_ '+str(thing)+ ' _|\n')
        return ret
