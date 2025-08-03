# 두 수 비교하기
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

num1,num2 = map(int,input().split()) # 두 수를 입력받음

if num1 > num2: # num1이 num2보다 크면, >
    print('>')
elif num1 < num2: # num1이 num2보다 작으면, <
    print('<')
else: # num1과 num2가 같으면, ==
    print('==')

