import employee


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


def write_employee_data(employee_dict, filename):
    file = open(filename, 'w')
    for item in employee_dict:
        file.write(employee_dict[item].get_name() + ',' + employee_dict[item].get_id() + ',' +
                   employee_dict[item].get_department() + ',' + employee_dict[item].get_job_title() + '\n')
    file.close()