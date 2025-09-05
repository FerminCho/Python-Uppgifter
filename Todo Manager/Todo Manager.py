import os

def choose_command():
    while True:
        cmd = input("> ")
        if cmd != "add" and cmd != "sub" and cmd != "mul" and cmd != "div":
            print("ERROR unknown command")
            input("Press Enter to continue...")
            os.system('cls')
        else:
            break
    return cmd

file = open("data.json", "r")
content = file.read()
file.close()

def main():
    todos = []
    cmd = choose_command()
    if cmd.lower() == "a":
        todo = input("Todo: ")
        todos.append({
            "name": todo,
            "checked": False,
        })


if __name__ == "__main__":
    main()
