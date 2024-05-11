# 파이썬프로그래밍 강의 10주차 과제

# 사용자 정의 함수부
def search(dic, productName) : # index() 메서드
    #(1)
    # if productName not in dic:
    #     return f'장바구니에 {productName}은(는) 없습니다.'
    
    #(2)
    if dic.get(productName) == None :
        return f'장바구니에 {productName}은(는) 없습니다.'
    
    return f'{productName}은(는) {dic[productName]}개 담겨 있습니다.'

# 주 프로그램부
print('[구입]')
shopping_bag = {}
while True :
    item = input('상품명? ')
    if item == '' :   
        break
    amount = int(input('수량은? '))
    shopping_bag[item] = amount
    print(f'장바구니에 {item} {shopping_bag[item]}개가 담겼습니다.\n')

print(f'\n>>> 장바구니 보기: {shopping_bag}')

print('\n[검색]')
item = input('장바구니에서 확인하고자 하는 상품은? ')
print(search(shopping_bag, item))
