msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

memory = 0.0


def take_input():
    operations = ['+', '-', '*', '/']

    while True:
        print(msg_0)
        x, operation, y = input().split()

        if x == 'M':
            try:
                y = float(y)
                x = memory
            except ValueError:
                print(msg_1)
                continue
        elif y == 'M':
            try:
                x = float(x)
                y = memory
            except ValueError:
                print(msg_1)
                continue
        else:
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


def is_one_digit(num):
    if num.is_integer():
        num = int(num)
        if -10 < num < 10:
            return True
    return False


if __name__ == "__main__":

    while True:
        x, operation, y = take_input()
        result = make_calculations(x, operation, y)
        if result is False:
            continue
        print(float(result))

        while True:
            print(msg_4)
            answer = input()
            if answer in ['y', 'n']:
                break

        if answer == 'y':
            memory = result

        while True:
            print(msg_5)
            answer = input()
            if answer in ['y', 'n']:
                break

        if answer == 'n':
            break








