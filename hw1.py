# 파이썬프로그래밍 강의 2주차 과제
#  사용자로부터 원의 반지름을 정수로 입력받아
#  그 원의 넓이를 구하는 프로그램을 구하는 프로그램을 작성하자
def get_radius(prompt) :
    r = int(input(prompt))
    return r

def get_circle_area(radius) :
    circle_area = 3.14 * radius * radius
    return circle_area

num = '넓이를 구하고자 하는 원의 반지름은? '
result = get_radius(num)
s = get_circle_area(result)

print('반지름', result,'인 원의 넓이 =', '3.14 x', result,'x', result, '=', s )
