# 부호 연산자
#산술 연산자
'''
floating point(부동소수점) 방식의 연산
나눗셈 몫은 실수형으로 출력
'''

    # 실습 예제 (1)
'''
a = int(input('피젯수를 정수로 입력하세요: '))
b = int(input('젯수를 정수로 입력하세요: '))
print('몫 =', a // b)
print('나머지 =', a % b)
'''

    # 실습 예제 (2) 사용자 정의 함수로
'''
def show_division(dividend, divisor) :
    quotient = dividend // divisor
    remainder = dividend % divisor
    print('몫 =', quotient)
    print('나머지 =', remainder)

a = int(input('피젯수를 정수로 입력하세요: '))
b = int(input('젯수를 정수로 입력하세요: '))
show_division(a, b)
'''

        # (2) 추가 연습 : 인수의 위치 변환
'''
def show_division(dividend, divisor) :
    quotient = dividend // divisor
    remainder = dividend % divisor
    print('몫 =', quotient)
    print('나머지 =', remainder)
    print('-----------')

a = int(input('피젯수를 정수로 입력하세요: '))
b = int(input('젯수를 정수로 입력하세요: '))
show_division(dividend = a, divisor = b)
show_division(dividend = b, divisor = a)
show_division(divisor = b, dividend = a)
show_division(divisor = a, dividend = b)
'''

    # 임시변수

n1 = 10
n2 = n1 + 4
'''
이때 n1에 4를 더하여 n2에 할당되는가?
= 그렇다. n2 <= 14 <= 10 + 4와 같은 과정으로 할당된다.
'''

    # 다중 대입문 - 복습 필요
'''
x = y = z = 1 # 세 변수에 각각 1이 할당됨
x, y = 1, 2 # 두 변수에 각각 순서대로 1, 2가 할당됨
x, y = y, x # 변수값 맞교환. y값이 x값에 할당되고 x값이 y값에 할당됨
'''

# 축약 대입 연산자 - 복습 필요
'''
자기할당문을 더 간략하게 표현하기 위한 연산자. 고유한 연산자로 취급한다.
n -= 2
n += 2
%=
**= 
'''

    # 실습예제 : 거스름돈 계산
# 가정(1) - payment>=total_cost, 즉 지불받은 금액은 항상 총구매비용 이상이다
# 가정(2) - 물건값과 잔돈은 모두 1,000원권과 5,000원권으로 지불한다
'''
total_cost = int(input('구매한 물건의 총구매 금액은? '))
payment = int(input('고객으로부터 지불받은 금액은? '))
change = payment - total_cost

def show_change(a) :
    print('잔돈:', a, "원 입니다.")
    n5000 = a // 5000
    a %= 5000

    n1000 = a // 1000

    print('>5000원권', n5000, '장')
    print('>1000원권', n1000, '장')

show_change(change)
'''

# 비트 연산자 - 복습 필요
    # 비트 연산자는 비트 논리연산과 비트 시프트 논리연산 두 가지 연산법이 존재
'''
n1 = 0b10101101
n2 = 0b00001111
print(bin(n1&n2))

.... 

n3 = 0b00001111
print(bin(n3 >> 2)) # 00000011, 3(=15 // 2**2)
print(bin(n3 << 2)) # 00111100, 60 (=15 * (2**2))
'''

# 연산자 우선순위
    # 어떤 연산자를 먼저 처리할 것인가?
'''
()로 감싼 연산이 가장 먼저 처리된다.
2*(2+3)*5의 경우
2+3 먼저, 그다음에 2랑 곱하고 마지막으로 5와 곱해 출력한다
'''
# 연산자 결합규칙
    # 연산자의 우선순위

# 연습문제 4.1, 4.2 - 화씨온도->섭씨온도 변환하기
'''
def fahrenheit_to_celsius(number) :
    C = 5/9*(number-32)
    return C

def get_real(prompt) :
    n1 = float(input(prompt))
    return n1

result = get_real('변환하고자 하는 화씨온도? :')
C = fahrenheit_to_celsius(result)
print('화씨', result,'도는 섭씨', C,'도')
'''
# 연습문제 4.3 - 초 단위 정리 문제 - 복습 필요
'''
def convert_time(s) :
    t1 = s / 60 # 분 단위로 변환
    s1 %= 60 # 분 단위로 변환되지 못한 초 단위
    t2 = t1 / 60 # 시간 단위로 변환
    t1 %= 60 # 시간 단위로 변환되지 못한 분 단위

    print(s,'초는', t2,'시간',t1

def get_integer(prompt) :
    res = int(input(prompt))
    return res

result = get_integer('변환하고자 하는 시간(초)? :')
convert_time(result)
'''
'''
def convert_time(sec) :
    h = sec // 3600
    s = sec % 3600
    m = s // 60
    s = s % 60
    print(sec, '초는', h,'시간', m,'분', s, '초이다.')

def get_integer(prompt) :
    res = int(input(prompt))
    return res

result = get_integer('변환하고자 하는 시간(초)? :')
convert_time(result)
'''
# 연습문제 4.6
def set_all_bits(n) :
    return (1 << n) - 1 # ob1000 - 1 = 0b111 임을 이용 
    
def get_integer(prompt) :
    res = int(input(prompt))
    return res

result = get_integer('설정할 비트 수는? :')
b = set_all_bits(result)
print(b)

# 비교(관계)연산자
# 논리 연산자
