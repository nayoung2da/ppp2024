import math

print("degree  sin(x)  cos(x)  tan(x)")
print("=" * 40)

degrees = [0, 30, 45, 60, 90]
for val in degrees:
    a = math.sin(math.pi * (val / 180))
    b = math.cos(math.pi * (val / 180))
    c = math.tan(math.pi * (val / 180))
    print(f"{val:2d}      {a:.4f}  {b:.4f}  {c:.4f}")