# 파이썬프로그래밍 강의 6주차 과제
# 사용자로부터 세 자릿수 이하의 10진 정수 하나를 입력받아
#각 자릿수를 한글로 읽어주는 프로그램 작성
# *유효한 정수만 입력됨을 가정

# 사용자 정의 함수부
def read_single_digit(number) :
    if number == 0 :
        return '영'
    elif number == 1 :
        return '일'
    elif number == 2 :
        return '이'
    elif number == 3 :
        return '삼'
    elif number == 4 :
        return '사'
    elif number == 5 :
        return '오'
    elif number == 6 :
        return '육'
    elif number == 7 :
        return '칠'
    elif number == 8 :
        return '팔'
    elif number == 9 :
        return '구'

def read_number(num) :
    if num < 10 :
        return f'{read_single_digit(num)}'
    
    elif num < 100 :
        digit1 = num % 10
        digit2 = (num - digit1) / 10
        return f'{read_single_digit(digit2)} {read_single_digit(digit1)}'
    
    else :
        digit1 = num % 10
        digit2 = (num - (int(num / 100)*100 + digit1)) / 10 # ex) num == 123, (123 - (int(1.23)*100 + 3)) / 10 = 2
        digit3 = (num - (digit2*10 + digit1)) / 100 # ex) num == 123, (123 - (2*10 + 3)) / 100 = 1
        return f'{read_single_digit(digit3)} {read_single_digit(digit2)} {read_single_digit(digit1)}'
     
'''
def read_number(n) :
    d1 = n % 10
    n //= 10
    d10 = n % 10
    n //= 10
    read_single_digit(n)
    read_single_digit(d10)
    read_single_digit(d11)

    num = input
    read_number(num)
'''
# 주 프로그램부
decimal_number = int(input('세 자리 정수 입력 : ')) 

print(read_number(decimal_number))