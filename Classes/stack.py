# ------------------
# Stack Class
# ------------------
class Stack: 
    
    # Constructor Function
    def __init__(self):
        self.__list= [] # private variable

    def isEmpty(self):
        return self.__list == []
    
    def getList(self):
        return self.__list
 
    def size(self):
        return len(self.__list)
 
    def clear(self):
        self.__list.clear() 
 
    def push(self, item): 
        self.__list.append(item) 
 
    def pop(self): 
        if self.isEmpty(): 
            return None
        else:
            return self.__list.pop() 
 
    def get(self): 
        if self.isEmpty(): 
            return None
        else:
            return self.__list[-1] 
 
    def __str__(self):
        return "".join(self.__list)