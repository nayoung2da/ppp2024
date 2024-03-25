mart = {"우유":2800, "계란":300, "빵":1200, "물":1700}

cart = []
cart.append("우유")
cart.append("물")

total_cost = 0
for item in cart:
    total_cost += mart[item]

print(f"담은 상품은 {cart}입니다.")
print(f"총 구매금액은 {total_cost:,}원입니다.")