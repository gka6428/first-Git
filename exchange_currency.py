# 환율 변환 처리 모듈
#
exchange_rate = 0

# 1달러에 대한 원화값 입력받아 환율을 전역변수 exchange_rate에 저장하는 함수
def set_rate(won) :
    global exchange_rate
    exchange_rate = won

# set_rate함수가 실행된 후 환율을 출력하는 함수
def get_rate() :
    return exchange_rate

# 원화를 달러화로
def to_dollar(won) :
    return won / exchange_rate

# 달러화를 원화로
def to_won(dollar) :
    return dollar * exchange_rate

# 테스트
def main() :
    print("### 환율 변환 모듈 테스트 ###")
    set_rate(1010)
    print('오늘의 환율은', get_rate(), '입니다.')
    print('2020원 =', to_dollar(2020),'달러')
    print('2달러 =', to_won(2), '원')

if __name__ == '__main__':
    main()
