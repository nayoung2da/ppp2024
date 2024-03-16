x1 = int(input("점1의 x좌표를 입력하세요. : "))
y1 = int(input("점1의 y좌표를 입력하세요. : "))
x2 = int(input("점2의 x좌표를 입력하세요. : "))
y2 = int(input("점2의 y좌표를 입력하세요. : "))

distance = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
print("점 ({}, {})과 점 ({}, {}) 사이의 거리는 {}이다.".format(x1, y1, x2, y2, distance))