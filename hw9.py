# 클래스 정의부
class Point :
    def __init__(self, x=0, y=0) :
        self.x = x
        self.y = y

    def show(self) :
        print(f'({self.x}, {self.y})')

    def set(self, x, y) :
        self.x = x
        self.y = y

    def get(self) :
        return (self.x, self.y)
    
class Rectangle :
    def __init__(self, x1, y1, x2, y2) :
        self.lt = Point(x1, y1)
        self.rb = Point(x2, y2)

    def getWidth(self) :
        width = self.rb.x - self.lt.x # self.x2 - self.x1? & 객체의 속성값의 속성값?
        return width
    
    def getHeight(self) :
        height = self.rb.y - self.lt.y
        return height

    def getArea(self) :
        area = self.getWidth() * self.getHeight()
        return area

    def getPerimeter(self) :
        perimeter = 2 * (self.getWidth() + self.getHeight())
        return perimeter

    def show(self) :
        print(f'좌측 상단 꼭짓점이 {self.lt.get()}이고, 우측 하단 꼭짓점이 {self.rb.get()}인 직사각형입니다.')

# 사용자 정의 함수부

# 주 프로그램부
r1 = Rectangle(5, 5, 20, 10)

a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
