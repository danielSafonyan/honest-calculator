msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

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


def lazy_check(x, operation, y):
    msg = ''

    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1 or y == 1) and operation == '*':
        msg += msg_7
    if (x == 0 or y == 0) and operation in ['*', '-', '+']:
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)

if __name__ == "__main__":

    while True:
        x, operation, y = take_input()
        lazy_check(x, operation, y)
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








