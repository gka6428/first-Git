import exchange_currency as Erate

# 주 프로그램부
rate = int(input('$1에 대한 오늘의 환율은? '))
Erate.set_rate(rate)

dollar = int(input('원화로 변환할 달러화 액수는? '))
print(dollar, '달러는', Erate.to_won(dollar), '원입니다.')

won = int(input('달화로 변환할 원화 액수는? '))
print(won, '달러는', Erate.to_dollar(won), '달러입니다.')