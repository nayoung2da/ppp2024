def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \003[38;2;255;255;255m".format(r, g, b, text)

print(colored(0, 255, 0,"우나영님 안녕하세요."))