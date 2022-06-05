msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."


def take_input():
    operations = ['+', '-', '*', '/']

    while True:
        print(msg_0)
        x, operation, y = input().split()

        try:
            x = int(x)
            y = int(y)
        except ValueError:
            try:
                x = float(x)
                y = float(y)
            except ValueError:
                print(msg_1)
                continue

        if operation not in operations:
            print(msg_2)
            continue
        return x, operation, y


def make_calculations(x, operation, y):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        if y == 0:
            print(msg_3)
            return False
        else:
            return x / y


if __name__ == "__main__":

    while True:
        x, operation, y = take_input()
        result = make_calculations(x, operation, y)
        if result is not False:
            print(float(result))
            break






