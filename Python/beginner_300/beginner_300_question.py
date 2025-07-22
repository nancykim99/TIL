# Q1
print('Hello World')

# Q2
print("Mary's cosmetics")

# Q3
print('신씨가 소리질렀다. "도둑이야".')

# Q4
print('C:Windows')

# Q5
print("안녕하세요.\n만나서\t\t반갑습니다.")
# \n : 엔터
# \t : tab

# Q6
print("오늘은", "일요일")
# 여러 값을 출력 시, 쉼표로 구분해주면 됨. (사이에 공백이 생김)

# Q7
print("naver;kakao;sk;samsung")
print("naver", "kakao", "samsung", sep=";")
# print 함수의 sep 인자로 ";" 입력하여, 한 칸의 공백대신, ":"이 출력됨
# sep(separation) : 분리하여 출력함. 구분자

# Q8
print('naver', 'kakao', 'sk', 'samsung', sep='/')

# Q9
print('first', end='');print('second')
# end : 그 뒤의 출력값과 줄바꿈을 하지 않고 이어서 출력함
# end에 입력시, sep과 비슷한 기능을 함

# Q10
print(5/3)

# Q11
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

# Q12
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

# Q13
s = "hello"
t = "python"

print(f'{s}! {t}')
print(s+"!", t)

# Q14
2 + 2 * 3
# 8

# Q15
a = '132'
type(a)
# <class 'str'>

# Q16
num_str = '720'
num_str = int(num_str)
print(num_str)
# 720

# Q17
num = 100
num = str(num)
print(num, type(num))
# 100 <class 'str'>

# Q18
num = '15.79'
num = float(num)
print(num, type(num))
# 15.79 <class 'float'>

# Q19
year = '2020'
print(int(year)-3) # 2017
print(int(year)-2) # 2018
print(int(year)-1) # 2019

# Q20
air_con = 48584
whole_price = air_con * 36
print(whole_price)
# 1749024