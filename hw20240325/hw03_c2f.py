def c2f(t_c):
    temp_f = t_c * 9/5 + 32
    print("{}C ==> {}F".format(t_c, temp_f))

def main():
    t_c = int(input("화씨 온도로 변환할 섭씨 온도를 입력해주세요. : "))
    c2f(t_c)
    
if __name__=="__main__":
    main()