def main():
    shapes = []

    shapes.append(Rectangle(5, 3))
    shapes.append(Triangle(5, 2))

    for shape in ahapes:
        print(shape)
        print(shape.area())
        print(shape.perimeter())


if __name__ == "__main__":
    main()