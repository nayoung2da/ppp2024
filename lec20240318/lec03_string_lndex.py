text = input("영어 단어를 입력하세요.")

print('입력한 문자는 "{}"입니다.'.format(text))

#영단어를 입력 받아서, 글자수를 출력하시오.
print(len(text))

#대문자로 변환하여 출력하시오.
print(text.upper())

#소문자로 변환하여 출력하시오.
print(text.lower())

#출력내용을 구분하기 위해 "===="와 같이 "="가 30개를 써서 출력하시오.
print("=" * 30)

#첫 3글자를 출력하시오.
print(text[:3])

#마지막 2글자를 출력하시오.
print(text[-2:])

#5번째 글자를 출력하시오.
print(text[4])

#문자열 뒤집기
print(text[::-1])