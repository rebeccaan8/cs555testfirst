stringOfInputs = input("Enter items separated by commas: ")

# do error checking here to see if inputs are correct

itemList = stringOfInputs.split(',')

sortedList = sorted(itemList)
print(sortedList)
