import os
import json


def choose_command():
    while True:
        cmd = input("> ")
        if cmd.lower() != "a" and cmd.lower() != "c" and cmd.lower() != "d" and cmd.lower() != "s" and cmd.lower() != "l" and cmd.lower() != "x":
            print("ERROR unknown command")
            input("Press Enter to continue...")
            os.system('cls')
        else:
            break
    return cmd


def show_error(type):
    if type == "cmd":
        print("ERROR unknown command")
    elif type == "index":
        print("ERROR invalid index")
    input("Press Enter to continue...")
    os.system('cls')


file = open("data.json", "r")
content = file.read()
file.close()


def main():
    todos = []
    while True:
        index = 0
        os.system('cls')
        for entry in todos:
            if entry["checked"]:
                check_box = "[X]"
            else:
                check_box = "[ ]"
            print(str(index) + " | " + check_box + " " + entry["name"])
            index += 1

        cmd = input("> ")
        cmd = cmd.lower()
        if cmd.lower() != "a" and cmd.lower() != "c" and cmd.lower() != "d" and cmd.lower() != "s" and cmd.lower() != "l" and cmd.lower() != "x":
            show_error("cmd")
            continue

        if cmd == "a":
            todo = input("Todo: ")
            todos.append({
                "name": todo,
                "checked": False,
            })
            continue
        elif cmd == "c" and len(todos) > 0:
            check_index = input("Index > ")
            try:
                todos[int(check_index)]["checked"] = True
            except (IndexError, ValueError):
                show_error("index")
                continue
        elif cmd == "d":
            del_index = input("Index >")
            try:
                todos.pop(int(del_index))
            except (IndexError, ValueError):
                show_error("index")
                continue
        elif cmd == "s":
            with open("data.json", "w") as f:
                json.dump(todos, f)
        elif cmd == "l":
            with open("data.json", "r") as f:
                todos = json.load(f)

        elif cmd == "x":
            os.system("cls")
            print("Program exited")
            exit()



if __name__ == "__main__":
    main()
