# 파이썬 9주차 과제
#  수량 저장/출력 기능 추가

print('[구입]')
shopping_bag = {}
while True :
    item = input('상품명? ')
    if item == '' :   
        break
    amount = int(input('수량은? '))
    shopping_bag[item] = amount
    print(f'장바구니에 {item}(이)가 담겼습니다.\n')

print(f'\n>>> 장바구니 보기: {shopping_bag}')
print('\n[검색]')
item = input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{item}은(는) {shopping_bag[item]}개 담겨 있습니다.')

