
# CSP 017
# Final Project - Milestone #2

data = []
choice = None

def sort():
    global choice
    if (choice == 0) or (choice == 1) or (choice == 2):
      sortD = sorted(data, key = lambda r:r[choice], reverse = True)
    else:
      sortD = sorted(data, key = lambda r:(int(r[choice])), reverse = True)
      
    counter = 0
    print("Top 5 Items:\n")
    for count in range(5):
        counter+=1
        print("     {}| {}  {}".format(counter, sortD[count][1],
                                 sortD[count][choice]))
    
# Defines the print menu function for simplicity
def printmenu():
            print('Select from the following options: \n \t1) Category' +
      '\n \t2) Item \n \t3) Serving Size \n \t4) Calories' +
      '\n \t5) Calories from Fat \n \t6) Total Fat' +
      '\n \t7) Cholestrol \n \t8) Sodium \n \t9) Carbohydrates' +
      '\n \t10) Protein \n \t11) Sugars \n \t12) Quit')
            
# Defines the input function
def choices():
    global choice
    while True:
        try:
            # Gives the user the option to chose which command 
            choice = int(input('Enter Number Command: '))
        except:
            print('Error... that was not a valid input.')
            
        # Depending on the choice the user selects
        # the program will display accordingly
        if choice == 1:
            print('Category: ')
            # Creates a new line a reprints menu
            print('\n')

        elif choice == 2:
            print('Item: ')
            print('\n')


        elif choice == 3:
            print('Serving Size: ')
            print('\n')

        elif choice == 4:
            print('Calories: ')
            print('\n')


        elif choice == 5:
            print('Calories from Fat: ')
            print('\n')


        elif choice == 6:
            print('Total Fat: ')
            print('\n')


        elif choice == 7:
            print('Cholestrol: ')
            print('\n')


        elif choice == 8:
            print('Sodium: ')
            print('\n')

        elif choice == 9:
            print('Carbohydrates: ')
            print('\n')


        elif choice == 10:
            print('Protein: ')
            print('\n')


        elif choice == 11:
            print('Sugars: ')
            print('\n')


        elif choice == 12:
            print('Program now exitting...')
            exit()

        # If the choice being made is outside of the menu
        # it will display this error message
        else:
            print('Invalid number selection! Try Again.')
            print('\n')

        sort()    
        printmenu()


infile = open("Mac_menu.csv", "r")
infile.readline()
for line in infile:
  line = line.strip("\n")
  result = tuple(line.split(","))
  data.append(result)
infile.close()
                        
# Calls Function & Prints out the options and different choices
printmenu()

# Calls the input function
choices()


