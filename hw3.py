from hw3modules import get_fixed_price as getFP

# 사용자 정의 함수부
def ask_sale_price(product_name) : # 매개변수 자료형은 문자열이라 가정함
    a = product_name + ' 상품의 할인된 가격은?'
    sale_price = int(input(a))
    return sale_price

# 주 프로그램부
sale_rate = int(input('할인율은?'))

result1 = getFP(sale_rate, ask_sale_price('A'))
result2 = getFP(sale_rate, ask_sale_price('B'))
print('A 상품의 정가는', result1, '원')
print('B 상품의 정가는', result2, '원')