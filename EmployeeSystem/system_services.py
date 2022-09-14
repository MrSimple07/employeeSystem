import employee
import validate


def read_employee_data(filename):
    employee_data_dict = {}
    file = open(filename, 'r')
    line = file.readline().rstrip('\n')

    while line != '':
        data_list = line.split(',')

        job_title = data_list.pop()
        department = data_list.pop()
        id_number = data_list.pop()
        name = data_list.pop()

        employee_data_dict[id_number] = employee.Employee(name, id_number, department, job_title)

        line = file.readline().rstrip('\n')

    file.close()

    return employee_data_dict


def write_employee_data(employee_dict):
    file = open('employee_data_new.txt', 'w')
    for item in employee_dict:
        file.write(employee_dict[item].get_name() + ',' + employee_dict[item].get_id() + ',' +
                   employee_dict[item].get_department() + ',' + employee_dict[item].get_job_title() + '\n')
    file.close()


def select_operation(employee_dict):
    user_input = 0
    while not user_input == 5:
        display_menu()
        user_input = int(validate.user_selection(input('Select an option (1-5): ')))

        if user_input == 1:
            look_up_employee(employee_dict)
        elif user_input == 2:
            add_new_employee(employee_dict)
        elif user_input == 3:
            change_existing_employee_data(employee_dict)
        elif user_input == 4:
            delete_employee(employee_dict)
        else:
            print('Goodbye!')


def display_menu():
    print('-----------Menu------------')
    print('(1) Look up an employee')
    print('(2) Add a new employee')
    print('(3) Change information for an existing employee')
    print('(4) Delete an employee')
    print('(5) Quit')


def look_up_employee(employee_dict):
    id_number = input('Enter employee ID number: ')
    print(employee_dict.get(id_number, 'ID number is not valid.'), '\n')


def add_new_employee(employee_dict):
    print('Add new employee:')
    name = input('Enter employee name: ').title()
    id_number = validate.id_number(input('Enter 5-digit ID number: '))
    department = input('Enter department: ').title()
    job_title = input('Enter job title: ').title()

    employee_dict[id_number] = employee.Employee(name, id_number, department, job_title)


def change_existing_employee_data(employee_dict):
    print('CHANGE EMPLOYEE DATA')
    employee_number = validate.key_in_dictionary(input('Enter employee number: '), employee_dict)

    print('\n--------Menu---------')
    print('Option 1: Display employee data: ')
    print('Option 2: Change name')
    print('Option 3: Change department')
    print('Option 4: Change job title')
    print('Option 5: Exit module')

    option = validate.user_selection(int(input('Enter option (1-5): ')))

    if option == 1:
        print(employee_dict[employee_number])
    elif option == 2:
        employee_dict[employee_number].set_name(input('Enter new name: '))
    elif option == 3:
        employee_dict[employee_number].set_department(input('Enter new department: '))
    elif option == 4:
        employee_dict[employee_number].set_job_title(input('Enter new job title: '))
    else:
        {}


def delete_employee(employee_dict):
    employee_number = validate.key_in_dictionary(input('Enter employee number: '), employee_dict)
    print('YOU WILL DELETE THE FOLLOWING EMPLOYEE:')
    print(employee_dict[employee_number])
    choice = validate.y_or_n(input('Would you like to perform this action? (Y/N): '))
    if choice.lower() == 'y':
        del employee_dict[employee_number]