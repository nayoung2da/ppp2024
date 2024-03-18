numbers = [10, 20, 30, 40]
numbers.append(100)    #시퀀스 끝에 100을 추가
print(numbers)
numbers.insert(4, 50)   #시퀀스의 4번 위치에 50을 삽입
numbers.extend([101, 102, 103])
numbers.remove(40)
numbers.clear()