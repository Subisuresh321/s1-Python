class rectangle():
    def __init__(self, length,breadth):
        self.__length = length
        self.__breadth = breadth
        self.__area=length*breadth
        
    def __lt__(self,other):
        if self.__area < other.__area :
            print (f"{other.__area} is greater")
        else:
             print (f"{self.__area} is greater")
rect1=rectangle(50,10)
rect2=rectangle(5,20)
rect1<rect2

