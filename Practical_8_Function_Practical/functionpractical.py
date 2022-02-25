def employee(*emp):

    print('Company Name :-', emp[0])
    print('Employee Name :-', emp[1])
    print('Employee id :-', emp[2])
    print('Employee Mobile No.:-', emp[3])
    print('Employee Address :-', emp[4])
    print('Employee Position:-', emp[5])
    print('Employee Salary :-', emp[6])
    print('Employee Total Income:-', emp[7])


inpt = int(input('Enter how many id do you want to enter:-'))

for x in range(inpt):
    cname = input("company name:-")
    ename = input("employee name:-")
    eid = input("employee id:-")
    enum = int(input("mobile no.:-"))
    add = input("Address:-")
    pos = input("position:-")
    salary = int(input("salary:-"))
    ta = salary * 0.02
    da = salary * 0.05
    hra = salary * 0.2
    pf = salary * 0.18
    tinc = salary + ta + da + hra - pf
    print('')
    employee(cname, ename, eid, enum, add, pos, salary, ta, da, hra, pf, tinc)
