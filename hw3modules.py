#정가 계산기
def get_fixed_price(sale_rate, sale_price) :
    fixed_price = sale_price * 100 / (100 - sale_rate)
    return fixed_price
