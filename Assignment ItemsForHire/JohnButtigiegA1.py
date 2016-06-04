#This allows the program to be exited when the user chooses to
import sys

def load_items():
    returnarray = []
    #Open, read and transfer the lines in data to the memory variable
    data_file = open("items.csv")

    for line in data_file:
        values = line.split(",")
        returnarray.append([values[0], values[1], values[2], values[3]])

    #stores the data in returnarray and returned the array.
    return returnarray


def list_items(data_lines):
    count = 0

    #print out each of the lines in data lines are formats it accordingly. If its out then a star is printed at the end
    for line in data_lines:
        if 'out' in line[3]:
            print("{3} - {0:<12} {1:<30} = {2}*".format(line[0], ("("+str(line[1])+")"), ("$"+str(line[2])), count))
        else:
            print("{3} - {0:<12} {1:<30} = {2}".format(line[0], ("("+str(line[1])+")"), ("$"+str(line[2])), count))

        #count on the end allows the number of the item on the list to be displayed
        count += 1


def hire_items(data_lines):
    count = 0
    numreturned = 0

    for line in data_lines:
        if 'in' in line[3]:
            print("{3} - {0:<12} {1:<30} = {2}".format(line[0], ("("+str(line[1])+")"), ("$"+str(line[2])), count))
            numreturned += 1
        count += 1

    #numreturned checks if there are 1 or more items available to hire, if there isn't it tells the user and exits the function
    if numreturned == 0:
        print('No items are currently on hire')
        return

    hirenum = int(input('Enter the number of an item to hire \n' '>>>'))

    #sets count back to zero
    count = 0
    available_checker = False
    for line in data_lines:
        #this checks which items the user has chosen by going through the list of items one by one.
        #if none is chosen available checker will be left false
        if hirenum == count and 'in' in line[3]:
            #Makes sure an item actually got hired
            available_checker = True
            #breaking out of loop once the program finds which item has been chosen or else the program will always choose the highest numbered item
            break

        count += 1

    #This continues the step from before if the code actually found the use hired something
    if (available_checker == True):
        print(line[0], 'hired for', "$"+str(line[2]))
        line[3] = 'out'
    else:
        print('That item is not available to hire')





def return_items(data_lines):
    count = 0
    numhired = 0

    for line in data_lines:
        if 'out' in line[3]:
            print("{3} - {0:<12} {1:<30} = {2}*".format(line[0], ("(" + str(line[1]) + ")"), ("$" + str(line[2])), count))
            numhired += 1

        count += 1

    #numhired checks if there are 1 or more items available to return, if there isn't it tells the user and exits the function
    if numhired == 0:
        print('There are no items to be returned')
        return


    hirenum = int(input('Enter the number of an item to return \n' '>>>'))

    # sets count back to zero
    count = 0
    available_checker = False
    for line in data_lines:
        if hirenum == count and 'out' in line[3]:
            # Makes sure an item actually got hired
            available_checker = True
            break
        count += 1



    if (available_checker == True):
        print(line[0], 'returned')
        line[3] = 'in'
    else:
        print('That item has not been hired')




def add_items(data_lines):
    name = input('Item name:')
    description = input('Description:')
    price = input('Price per day: $')

    data_lines.append([name, description, price, "in"])

    print(name, '('+description+'),', price, 'now available for hire')


def main():
    #This sets data_lines to the returnarray variable that got returned in the load_items() function
    data_lines = load_items()

    #Asks the user what they would like to do
    print('Welcome to Johns Items For Hire program!')
    print("What would you like to do? \n (L)ist all items \n (H)ire an item \n (R)eturn an item \n (A)dd new item to stock \n (Q)uit")
    choice = input('>>> ').upper()

   #While loop with if statements which always asks the user what they would like to do until they type Q which exits the program
    while choice != 'Q':
        if choice == 'L':
            list_items(data_lines)
        elif choice == 'H':
            hire_items(data_lines)
        elif choice == 'R':
            return_items(data_lines)
        elif choice == 'A':
            add_items(data_lines)

        #Asks again to prevent infinite looping
        print("What would you like to do? \n (L)ist all items \n (H)ire an item \n (R)eturn an item \n (A)dd new item to stock \n (Q)uit")
        choice = input('>>> ').upper()


    sys.exit()



main()