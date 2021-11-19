# YES/NO checker
def checker(value):
    if value.lower() == "yes":
        return True
    elif value.lower() == "no":
        return False
    else:
        return "Incorrect value"

sikl = True

while sikl:
    a = input("/: ")
    if a == "stop":
        sikl = False
        print("Program stopped...")
    result = checker(a)
    print(result)

