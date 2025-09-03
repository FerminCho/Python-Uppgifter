
print(".: MATHLETE v2.0 :.")
print("-------------------")

cardinality = 0
sum = 0

while True:
    input_value = input("> ")

    if input_value == "exit":
        break

    try:
        float(input_value)
    except ValueError:
        print("ERROR: invalid number")
        continue

    cardinality += 1
    sum += int(input_value)

print("-------------------")
print("Cardinality: " + str(cardinality))
print("Sum: " + str(sum))
if cardinality != 0:
    print("Mean value: " + str(sum/cardinality).rstrip("0").rstrip("."))
else:
    print("Mean value: undefined")
