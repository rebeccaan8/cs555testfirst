def alphabetize(stringOfInputs):

    # do error checking here to see if inputs are correct

    itemList = stringOfInputs.split(',')

    sortedList = sorted(itemList)
    return sortedList

def main():
    print("This is the main function.")
    stringOfInputs = input("Enter items separated by commas: ")
    alphabetize(stringOfInputs)
    print("The sorted list is:" + str(alphabetize(stringOfInputs)))

if __name__ == "__main__":
    main()

#input error checking
    # - check if input is empty
    # - check if input is a string
    # - check if input is a number
    # - check if input is a bunch of spaces
    # - check if input ends in a comma
    # - check if input starts with a comma
    # - check if input has any items that are blank/spaces
    # - remove all spaces from the front and end of the input