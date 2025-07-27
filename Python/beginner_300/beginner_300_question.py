# 01
print('Hello World')

# 02
print("Mary's cosmetics")

# 03
print('신씨가 소리질렀다. "도둑이야".')

# 04
print('C:Windows')

# 05
print("안녕하세요.\n만나서\t\t반갑습니다.")
# \n : 엔터
# \t : tab

# 06
print("오늘은", "일요일")
# 여러 값을 출력 시, 쉼표로 구분해주면 됨. (사이에 공백이 생김)

# 07
print("naver;kakao;sk;samsung")
print("naver", "kakao", "samsung", sep=";")
# print 함수의 sep 인자로 ";" 입력하여, 한 칸의 공백대신, ":"이 출력됨
# sep(separation) : 분리하여 출력함. 구분자

# 08
print('naver', 'kakao', 'sk', 'samsung', sep='/')

# 09
print('first', end='');print('second')
# end : 그 뒤의 출력값과 줄바꿈을 하지 않고 이어서 출력함
# end에 입력시, sep과 비슷한 기능을 함

# 10
print(5/3)

# 11
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

# 12
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

# 13
s = "hello"
t = "python"

print(f'{s}! {t}')
print(s+"!", t)

# 14
2 + 2 * 3
# 8

# 15
a = '132'
type(a)
# <class 'str'>

# 16
num_str = '720'
num_str = int(num_str)
print(num_str)
# 720

# 17
num = 100
num = str(num)
print(num, type(num))
# 100 <class 'str'>

# 18
num = '15.79'
num = float(num)
print(num, type(num))
# 15.79 <class 'float'>

# 19
year = '2020'
print(int(year)-3) # 2017
print(int(year)-2) # 2018
print(int(year)-1) # 2019

# 20
air_con = 48584
whole_price = air_con * 36
print(whole_price)
# 1749024

# 201
def print_coin():
    print("비트코인")

# 202
print_coin()

# 203

# 틀린 답
for i range(100):
    print_coin(i) # i를 왜 넣었니...

# 맞는 답
for i range(100): # 100번
    print_coin() # 함수 호출

# 204
def print_coins():
    for i in range(100):
        print("비트코인")

# 205
hello()
def hello():
    print("Hi")
# NameError: name 'hello' is not defined

# 답 : 함수 호출을 정의 하기 전에 해서

# 206
def message():
    print("A")
    print("B")

message()
print("C")
message()

# 답
# A
# B
# C
# A
# B

# 207
print("A")
def message():
    print("B")
print("C")
message()

# 답
# A
# C
# B

# 208
print("A")
def message1():
    print("B")
print("C")
def message2():
    print("D")
message1()
print("E")
message2()

# 답
# A
# C
# B
# E
# D








