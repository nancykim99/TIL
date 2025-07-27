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
for i in range(100):
    print_coin(i) # i를 왜 넣었니...

# 맞는 답
for i in range(100): # 100번
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

# 함수 호출을 정의 하기 전에 해서

# 206
def message():
    print("A")
    print("B")

message()
print("C")
message()

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

# A
# C
# B
# E
# D

# 209
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

# B
# A

# 210
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range(3):
        message2()
        print("C")
    message1()

message3()

# B
# C
# B
# C
# B
# C
# A

# 211
def 함수(문자열):
    print(문자열)

함수("안녕")
함수("Hi")

# 안녕
# Hi

# 212
def 함수(a, b):
    print(a + b)

함수(3, 4)
함수(7, 8)

# 7
# 15

# 213
def 함수(문자열):
    print(문자열)

함수()
#TypeError: 함수() missing 1 required positional argument: '문자열'

# 함수를 호출할 때 하나의 파라미터를 입력하지 않아서

# 214
def 함수(a, b):
    print(a + b)

함수("안녕", 3)
# TypeError: must be str, not int

# str과 int는 합할 수 없음

# 215

def print_while_smile(문자열):
    print(문자열 + ":D")

# 216

print_while_smile("안녕하세요")

# 217

def print_upper_price(number):
    print(number * 1.3)

# 218

def print_sum(x, y):
    print(x + y)

#219

# 틀린 답
def print_arithmetic_operation(x, y):
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)

# 맞는 답
def print_arithmetic_operation(x, y):
    print(x, "+", y "=" = x + y)
    print(x, "-", y "=" = x - y)
    print(x, "*", y "=" = x * y)
    print(x, "/", y "=" = x / y)

# 220

# 틀린 답
def print_max(x, y ,z):
    if x < y:
        if y < z:
            print(z)
        elif y > z:
            print(y)
    elif x > y:
        if x < z:
            print(z)
        elif x > z:
            print(x)

# 맞는 답
def print_max(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > c and b > a:
        print(b)
    else:
        print(c)

# 221

def print_reverse(string):
    print(string[::-1])

# 222

# 맞는 답
def print_score(score_list):
    print(sum(score_list)/len(score_list))

# 223

# 틀린 답
def print_even(num_list):
    print(num_list % 2 == 0)

# 맞는 답
def print_even(num_list):
    for v in num_list:
        if v % 2 == 0:
            print(v)

# 224
print_keys({"이름":"감말똥", "나이":30, "성별":0})

# 틀린 답
def print_keys(dictionary):
    print(dictionary.keys())

# 맞는 답
def print_keys(dic):
    for keys in dic.keys():
        print(keys)

# 225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

# 틀린 답
def print_value_by_key(dict):
    for keys in dict:
        print(dict[keys])

# 정답
def print_value_by_key(dict, key):
    print(dict[key])

# 226
print_5xn("아이엠어보이유알어걸")

def print_5xn(string):
    print(string[0:5])
    print(string[5:10])

# 정답
def print_5xn(line):
    chunk_num = int(len(line) / 5)
    for x in range(chunk_num + 1):
        print(line[x * 5: x * 5 + 5])

# print(line[0:5])
# print(line[5:10])
# print(line[10:15])
# ...

# range 함수 : 0부터 n-1까지 순회

# 227
printmxn("아이엠어보이유알어걸", 3)

# 틀린 답
def printmxn(line, num):
    for i in range(num):
        print(line[i * num : i * num + num])

# 정답
def printmxn(line, num):
    chunk_num = int(len(line) / num)
    for i in range(chunk_num + 1):m # 나눠서 +1 해야 남는 문자열까지 프린트 가능
        print(line[i * num : i * num + num])

# 228
calc_monthly_salary(12000000)

def calc_monthly_salary(num):
    monthly_salary = int(num / 12)
    return monthly_salary

# 229
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

# 답
# 왼쪽: 100
# 오른쪽: 200

# 230
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)

# 답
# 왼쪽: 200
# 오른쪽: 100

# 231
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
print (result)

# 답
# 에러?
# NameError: name 'result' is not defined
# 함수 내 사용한 변수는 함수 밖에서 접근 불가 > 계산한 값을 전달하기 위해 return 사용 필요

# 232
make_url("naver")

def make_url(string):
    return "www.", string, ".com"

# 233
make_list("abcd")

def make_list(string):
    list = []
    for str in string:
        list.append(str)
    return list

# 다른 답
def make_list (string) :
    return list(string)

# 234
pickup_even([3, 4, 5, 6, 7, 8])

# 틀린 답
def pickup_even(list):
    even_num = []
    for num in list:
        even_num.append(num % 2 == 0)
    return even_num

# 정답
def pickup_even(list):
    even_num = []
    for num in list:
        if num % 2 == 0:
            even_num.append(num)
    return even_num

# 235
convert_int("1,234,567")

# 답
def convert_int(string):
    return int(string.replace(',',''))

# 236
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

# 답
# 14
# 18
# 22

# 237
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

# 답
# 22

# 238
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

# 답 : 140

# 239
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

# 답 : 16

# 240
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)

# 답 : 28








