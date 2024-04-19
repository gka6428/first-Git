# 파이썬프로그래밍 5주차 과제
'''
한국에 방문하는 교포 지인에게 환영 메시지를 작성하고
이를 출력해 공항으로 가져가고자 한다.
▪ 영어로 된 이름을 입력받아 두 줄의 환영메시지를 완성
▪ 연습문제 6.4와 6.5의 사용자 정의 함수를 약간 변형하여 사용
▪ 첫 줄과 두 번째 줄 중긴줄을 기준으로 박스선 길이를 설정

nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
'''

# 사용자 정의 함수부
def rep_char(c, n) :
    print(c * n)

def draw_line_string(name) :
    msg1 = f'Hello, {name},'
    msg2 = 'Welcome to Seoul.'
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)

    rep_char('-', nstr + 2)
    print(msg1)
    print(msg2)
    rep_char('-', nstr + 2)

# 주 프로그램부
friend_name = input('Input his/her name: ')
draw_line_string(friend_name)