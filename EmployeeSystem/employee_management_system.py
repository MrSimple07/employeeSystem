import system_services
import file_services


def main():
    employee_dict = file_services.read_employee_data('employee_data.txt')
    print('EMPLOYEE MANAGEMENT SYSTEM')
    system_services.select_operation(employee_dict)
    file_services.write_employee_data(employee_dict, 'employee_data.txt')


main()