class Rectangle():
    def __init__(self, width, length):
        self.width=width
        self.length=length
        
    def perimeter(self):
        return ((self.width * 2) + (self.length * 2))


    
class Square():
    def __init__(self,s1):
        self.s1=s1
    
    def perimeter(self):
        return self.s1*4



Rect=Rectangle(2,3)
print(Rect.perimeter())

Squ=Square(2)
print(Squ.perimeter())




