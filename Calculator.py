import os
from xml.dom.minidom import NamedNodeMap

saved_calcs = []

def choose_math():
    while True:
        math = input("> ")
        if math != "add" and math != "sub" and math != "mul" and math != "div":
            print("Unknown operation " + (math))
            input("Press Enter to continue...")
            os.system('cls')
            show_saves()
        else:
            break
    return math

def check_value(num):
    try:
        float(num)
    except ValueError:
        print("Invalid float" + str(num))
        return True
    return False

def set_a():
    value = input("a = ")
    while check_value(value):
        value = input("a = ")
    return value

def set_b():
    value = input("b = ")
    while check_value(value):
        value = input("b = ")
    return value

def show_saves():
    for calc_str in saved_calcs:
        print(calc_str)

def main():
    while True:
        show_saves()
        print("\n")

        current_calc = choose_math()
        a = float(set_a())
        b = float(set_b())

        if current_calc == "add":
            ans = a + b
            text = str(a) + " + " + str(b) + " = " + str(ans)
            print(text)
            saved_calcs.append(text)
            os.system('cls')
        elif current_calc == "sub":
            ans = a - b
            text = str(a) + " - " + str(b) + " = " + str(ans)
            print(text)
            saved_calcs.append(text)
            os.system('cls')
        elif current_calc == "mul":
            ans = a * b
            text = str(a) + " * " + str(b) + " = " + str(ans)
            print(text)
            saved_calcs.append(text)
            os.system('cls')
        elif current_calc == "div":
            if b == 0 and a == 0:
                ans = "NaN"
            elif b == 0:
                ans = "Infinity"
            else:
                ans = a / b
            text = str(a) + " / " + str(b) + " = " + str(ans)
            print(text)
            saved_calcs.append(text)
            os.system('cls')

        if len(saved_calcs) > 3:
            saved_calcs.pop(0)

if __name__ == "__main__":
    main()
