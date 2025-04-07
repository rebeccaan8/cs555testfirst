def alphabetize(list):
    itemList = list.split(',')
    itemList = [item.strip() for item in itemList]

    sortedList = sorted(itemList)
    return sortedList


def inputCheck(list):
    if not list:
        return "Input is empty."

    if type(list) is not str:
        return "Input is not a string."

    if list.isspace():
        return "Input is just spaces."

    list = list.strip()
    if list.endswith(','):
        return "Input ends in a comma."

    for item in list.split(','):
        if item.isspace() or not item:
            return "Input has blank spaces and/or items."

    return "True"


def main():
    list = input("Enter items separated by commas: ")
    list = str(list)
    isValid = inputCheck(list)

    if (isValid == "True"):
        alphabetize(list)
        print("The sorted list is: " + str(alphabetize(list)))
        return
    else:
        print("Invalid input. " + isValid + " Please try again.")
        return    
    return


if __name__ == "__main__":
    main()