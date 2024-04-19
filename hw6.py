# 사용자 정의 함수부
def display_multiplication_table(number, index) :
    for cnt in range(number, number + 4) :
        print(f'{cnt} X {index} = {cnt * index:2d}', end='\t')
    print()
        
# 주 프로그램부
for i in range(1, 10) :
    display_multiplication_table(2, i)

print()

for i in range(1, 10) :
    display_multiplication_table(6, i)

''' 사용자 정의 함수를 사용하지 않는 경우 (for)
for i in range(1, 10) :
    for n in range(2, 6) :
        print(f'{n} X {i} = {n * i:2d}', end='\t')
    print()
        
print()

for j in range(1, 10) : 
    for k in range(6, 10) :
        print(f'{k} X {j} = {k * j:2d}', end='\t')
    print()
'''        


