import json

def main():

    with open("registrations.json", "r") as f1:
        regis = json.load(f1)
    with open("results.json", "r") as f2:
        results = json.load(f2)

    cmd = input("What to do? ")

    if cmd == "1":
        participant_number = int(input("Runner's number? "))
        runner_data = regis[participant_number]
        print(runner_data["name"] + "\n" + runner_data["city"] + "\n" + str(runner_data["number"]))
    elif cmd == "2":
        entered_time = int(input("Last participants faster than what (sec)? "))

        empty = True
        for time_entry in results:
            if time_entry["time"] < entered_time:
                empty = False
                runner_data = regis[time_entry["number"] - 1]
                rest = time_entry["time"] % 60
                minutes = time_entry["time"] // 60
                min_str = "min " + str(minutes) + "sec " + str(rest)
                print(str(runner_data["number"]) + "\n" + str(time_entry["time"]) + " " + min_str + "\n" + runner_data["name"] + "\n" + runner_data["city"] + "\n")
        if empty:
            print("Pleas select value greate than fastest time (1213 sec)")
    else:
        exit()


if __name__ == "__main__":
    main()
