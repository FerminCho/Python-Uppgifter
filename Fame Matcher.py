
class People:
    name = ""
    gender = ""
    hair_color = ""
    eye_color = ""

    def __init__(self, name, gender, hair_color, eye_color):
        self.name = name
        self.gender = gender
        self.hair_color = hair_color
        self.eye_color = eye_color


people_list = []
def main():
    people_list.append(People("Daniel Radcliffe", "male", "brown", "brown"))
    people_list.append(People("Ruper Grint", "male", "red", "blue"))
    people_list.append(People("Emma Watson", "female", "brown", "brown"))
    people_list.append(People("Selena Gomez", "female", "brown", "brown"))
    people_list.append(People("Angelina Jolie",  "female", "blond",  "blue"))
    people_list.append(People("Tom Hanks", "male", "brown", "brown"))
    people_list.append(People("Taylor Swift", "female", "blond", "green"))
    people_list.append(People("Margot Robbie", "female", "orange", "blue"))
    people_list.append(People("Jean-Claude", "male", "brown", "green"))


    print("Fame Matcher")
    print("------------\n")
    enterd_gender = input("Gender: ")
    enterd_hair_color = input("Hair color: ")
    enterd_eye_color = input("Eye color: ")
    print("\n------------")

    x = 0
    match_message = "\nMATCH: "
    for person in people_list:
        if enterd_gender == person.gender and enterd_hair_color == person.hair_color and enterd_eye_color == person.eye_color:
            if x == 1:
                match_message += ", "
            x = 1
            match_message += person.name

    if x == 1:
        print(match_message)
    else:
        print("\nERROR: Not match found")

if __name__ == "__main__":
    main()
