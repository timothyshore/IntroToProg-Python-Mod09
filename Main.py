# ------------------------------------------------------------------------ #
# Title: Assignment 09/Main Module
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Tim Shore,12.12.2020,Added code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]

Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))

# Show user a menu of options
while True:
    Eio.print_menu_items()
    menu_choice = Eio.input_menu_options()  # Get user's menu option choice
    print(menu_choice)

    if menu_choice.strip() == '1':  # Show user current data in the list of employee objects
        Eio.print_current_list_items(lstTable)
        continue

    if menu_choice.strip() == '2':  # Let user add data to the list of employee objects
        lstTable.append(Eio.input_employee_data())
        continue

    if menu_choice.strip() == '3':  # let user save current data to file
        Fp.save_data_to_file('EmployeeData.txt', lstTable)
        print('Data Saved!')
        continue

    if menu_choice.strip() == '4':  # let user exit program
        print('Good-bye!')
        break

    else:
        print('Not a valid selection. Try again!')

# Main Body of Script  ---------------------------------------------------- #