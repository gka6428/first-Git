# (1) 기초적인 사용자 정의 함수의 실행 과정
# 사용자 정의 함수의 구조
def hello() :
        print('hello world!')
        print('good job!')

# 사용자 정의 함수의 실행 방법
print('시작')
hello()
print('마침')

print('----------------------------')
# (2) assign operator(할당 연산자) '=' 의미
'''
변수_이름 = 초기값

'오른쪽 표현식의 결과값을 왼쪽에 넣음'을 의미함
* 그러나 할당시 기존에 변수가 갖고 있는 값은 유지되지 못하고 사라지므로 유의
'''

# (3) 변수의 개념 및 변수 선언, 여러 변수의 동시 선언
nStud, nProf = 9, 3
print(nStud)
print(nProf)

print('----------------------------')
# (4) 변수 값의 참조
num = 1004
print(num)
num = '천사'
print(num)

print('----------------------------')
# (5) 변수의 자료형 - type()으로 확인 가능
print(type(num))

print('----------------------------')

# (6) 매개변수(파라미터)를 갖는 함수 <- 매개변수를 갖는 함수는 반드시 호출시 인수를 지정해야 합니다
# 사용자 정의 함수부
def show_message(name) :
    print('hello', name, '님')

# 주 프로그램부
print('시작')
show_message('이찬수')
show_message('홍길동')
print('마침')

print('----------------------------')

# (7) 두 개 이상의 매개변수를 갖는 함수
# 사용자 정의 함수부
def kiki(msg, name) :
    print(msg, name, '님')

# 주 프로그램부
print('시작')
kiki('안녕','이찬수')
kiki('반가워요','홍길동')
print('마침')

print('----------------------------')

# (8) 매개변수 중 키워드 인수
'''
함수이름(매개변수명=인수값) :

이를 이용해 각 인수가 매개변수에 전달되는 차례를 변경할 수 있다.
'''
# 주 프로그램부
print('시작')
kiki(msg='안녕', name='이찬수')
kiki(name='이찬수', msg='안녕')
print('마침')

print('----------------------------')

# (9) 매개변수의 기본값을 갖는 함수
# 사용자 정의 함수부
def hihi(msg='안녕하세요', name='여러분') :
    print(msg, name, '님')

# 주 프로그램부
print('시작')
hihi('안녕', '고구마')
hihi(name='이찬수')
hihi('반가워요')
hihi(msg='반가워요')

print('----------------------------')

# (10) print()의 키워드 인수 sep='', end=''
#sep
print('life', 'is', 'too', 'short')
print('life', 'is', 'too', 'short', sep='.')

#end
print('life', 'is', end=' ')
print('too short')

print('----------------------------')

# (11)복귀와 반환값 return
'''
프로그래머에 의한 수동 복귀 처리가 가능함
'''

# (12)
# 사용자 정의 함수부
def pipi() :
    print('hello')
    return 'good bye'

# 주 프로그램부
print('시작')
result = pipi() # 함수의 반환값을 새로운 변수에 할당
print(result)
print('마침')

print('----------------------------')

# (13)
'''
print('당신의 이름은? ', end='')
name= input()
print('반가워요', name)

name = input('당신의 이름은? ')
print('반가워요', name, '님')
'''
print('반가워요', input('당신의 이름은? '))



































