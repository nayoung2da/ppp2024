class Cake:
    """케익을 나타내는 클래스"""
    coat = "생크림"

    def __init__(self, topping, price, candles=0):
        """인스턴스를 초기화한다."""
        self.topping = topping # 케익에 올린 토핑
        self.price = price # 케익의 가격
        self.candles = candles # 케익에 꽂은 초 개수

    def describe(self):
        """이 케익에 관한 정보를 화면에 출력한다."""
        print(f"이 케익은 {self.coat}으로 덮여 있습니다.")
        print(f"이 케잌의 토핑은{self.topping}입니다.")
        print(f"이 케잌의 가격은 {self.price:,d}원입니다.")
        if self.candles > 0:
            print(f"초가 {self.candles}개 꽂혀 있다.")

def main():
    cake_truck = []

    cake_truck.append(Cake("눈사람 사탕", 10000))
    cake_truck.append(Cake("한라봉", 9000, 8))

    for cake in cake_truck:
        print(cake.price)
        cake.describe()


if __name__ == "__main__":
    main()