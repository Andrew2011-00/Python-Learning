operations = ["+", "-", "*", "/"]
memory = 0

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
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

def is_one_digit(v):
    return isinstance(v, (int, float)) and -10 < v < 10 and v == int(v)

while True:
    print(msg_0)
    equation = input().split()

    if len(equation) != 3:
        print(msg_1)
        continue
    x_raw, op, y_raw = equation

    if op not in operations:
        print(msg_2)
        continue

    try:
        x = memory if x_raw == "M" else float(x_raw)
        y = memory if y_raw == "M" else float(y_raw)
    except ValueError:
        print(msg_1)
        continue

    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    if (x == 1 or y == 1) and op == "*":
        msg = msg + msg_7
    if (x == 0 or y == 0) and (op == "*" or op == "+" or op == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)

    try:
        if op == "+":
            calculation = x + y
        elif op == "-":
            calculation = x - y
        elif op == "*":
            calculation = x * y
        elif op == "/":
            if y == 0:
                raise ZeroDivisionError
            calculation = x / y

        print(calculation)
        print(msg_4)
        y_n1 = input().strip().lower()
        if y_n1 == "y":
            if is_one_digit(calculation):
                print(msg_10)
                y_n2 = input().strip().lower()
                if y_n2 == "y":
                    print(msg_11)
                    y_n3 = input().strip().lower()
                    if y_n3 == "y":
                        print(msg_12)
                        y_n4 = input().strip().lower()
                        if y_n4 == "y":
                            memory = calculation

                else:
                    pass
            else:
                memory = calculation

        print(msg_5)
        y_n5 = input().strip().lower()
        if y_n5 == "y":
            continue
        else:
            break

    except ZeroDivisionError:
        print(msg_3)