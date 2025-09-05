import json


def main():

    with open("registrations.json", "r") as f1:
        regis = json.load(f1)
    with open("results.json", "r") as f2:
        results = json.load(f2)

    cmd = input("What to do? ")

    if cmd == "1":
        participant_number = int(input("Runner's number? "))
        runner_data = regis[participant_number - 1]
        print(runner_data["name"] + "\n" + runner_data["city"] + "\n" + str(runner_data["number"]))
    elif cmd == "2":
        entered_time = int(input("Last participants faster than what (sec)? "))

        for time_entry in results:
            if time_entry["time"] > entered_time:
                runner_data = regis[time_entry["number"] - 1]
                print(str(runner_data["number"]) + "\n" + time_entry["time "] + "\n" + runner_data["name"] + "\n" + runner_data["city"])
    else:
        exit()


if __name__ == "__main__":
    main()
