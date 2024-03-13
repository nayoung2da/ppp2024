# temp_c = 30

# temp_c = input("온도를 입력하세요.")
# temp_c = int(temp_c)

temp_c = int(input("화씨 온도로 변환할 섭씨 온도를 입력해주세요. :"))
temp_f = (temp_c * 1.8) + 32
print("{}℃ => {}℉".format(temp_c, temp_f))