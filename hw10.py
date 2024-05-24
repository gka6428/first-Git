# 모듈 불러오기
import os 

# 사용자 함수 정의부
def input_scores():
    print('[점수 입력]')
    i = 1
    while True :
        num = int(input(f'#{i}? '))
        if num < 0:
            break
        scores.append(num)
        i += 1

def get_average(lst):
    total = 0
    for i in lst:
        total += i
    avg = total / len(lst)
    return avg
    
def show_scoers(lst):
    print('[점수 출력]')
    print('개인점수: ', end='')
    for i in lst:
        print(f'{i} ', end='')
    
# 주 프로그램부
filename = 'score.bin'
if os.path.exists(f'data/{filename}'):
    print('[파일 읽기]\n')
    with open(f'data/{filename}', 'rt', encoding='utf8') as file:
        print(file.read())
else:
    scores = []
    input_scores()
    show_scoers(scores)
    print(f'\n평균: {get_average(scores):.1f}')
    with open(f'data/{filename}', 'wt', encoding='utf8') as file:
        file.write('[점수 출력]\n')
        file.write('개인 점수: ')
        for i in scores:
            file.write(f'{i} ')
        file.write(f'\n평균: {get_average(scores):.1f}')
