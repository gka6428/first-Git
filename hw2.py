# 파이썬프로그래밍 3주차 과제
# 개념확인 과제 (연습문제 4.7)
# 사용자로부터 입력된 금액을 동전으로 교환하고자 할 때, 각 동전별 교환 개수를 출력한다.

# 용어 정리
''' 
account == 금액
balance == 잔액
nk (k는 자연수) == k원 동전의 개수 
'''

# 사용자 함수 정의부
def exchange(money) :
    n500 = money // 500 # 500으로 나누었을 때의 몫 == 500원 동전의 개수
    balance = money % 500 # 500으로 나누었을 때의 나머지(금액) == 다음 단위동전에 할당할 잔액

    n100 = balance // 100
    balance %= 100
    
    n50 = balance // 50
    balance %= 50
    
    n10 = balance // 10

    print('500원 동전의 개수:', n500)
    print('100원 동전의 개수:', n100)
    print('50원 동전의 개수:', n50)
    print('10원 동전의 개수:', n10)
          
def get_integer(prompt) :
    res = int(input(prompt))
    return res


# 주 프로그램부
account = get_integer('동전으로 교환하고자 하는 금액은? :')
exchange(account)
