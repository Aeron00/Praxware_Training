print('------------------------welcome to this page--------------------------\n')
print('**select any option from below for further interaction with this page**')
print('----------------------registration---------login----------------------\n')
selectoption = input('write your selected option here:-')
while True:
    if selectoption == "registration":
        print('Registration page')
        Name = input('Enter your name here:-')
        Email = input('Enter your email here:-')
        Password = input('Enter your login password here:-')
        Mobilenumber = int(input('Enter your mobile number here:-'))
        position = input('Enter your position here:-')
        print('Registration completed successfully')
        print('Do you want to register again')
        click = input('select an option\nYES or NO :-')
        while True:
            if click == 'YES':
                print('Register again here')
                break
            elif click == 'NO':
                print('do you want to login your account')
                print('select option yes or no')
                option = input('select option yes or no:')
                while True:
                    if option == 'yes':
                        print('Welcome to login page')
                        Email = input('Email id:-')
                        Password = input('Password:-')
                        print('login completed successfully')
                        print('***************************')
                        print('do you want to input data of students')
                        while True:
                            option1 = input('select option yes or no:')
                            if option1 == 'yes':
                                department = input('Enter department:-')
                                studentname1 = input('Enter student1 name :-')
                                studentfees1 = int(input(F'Enter {studentname1} fees ='))
                                studentname2 = input('Enter student2 name :-')
                                studentfees2 = int(input(F'Enter {studentname2} fees ='))
                                studentname3 = input('Enter student3 name :-')
                                studentfees3 = int(input(F'Enter {studentname3} fees ='))
                                studentname4 = input('Enter student4 name :-')
                                studentfees4 = int(input(F'Enter {studentname4} fees ='))
                                studentname5 = input('Enter student5 name :-')
                                studentfees5 = int(input(F'Enter {studentname5} fees ='))
                                print('\ndo you want add another information')
                                while True:
                                    add = input('select option yes or no:')
                                    if add == 'yes':
                                        option1 = 'yes'
                                    elif add == 'no':
                                        print('\nthank you!!!')
                                        break
                                    else:
                                        print('\nerror select option again')
                                print('For accessing your data select below clicks')
                                print(
                                    'click1 = for display all data\nclick2 = for display all admin info\nclick3 = show password')
                                while True:
                                    accessdata = input('write any one click here:-')
                                    if accessdata == 'click1':
                                        print('Admin details')
                                        print(F'name={Name}')
                                        print(F'Email={Email}')
                                        print('Password=********')
                                        print(F'Mobile Number={Mobilenumber}')
                                        print(F'Position={position}')
                                        print(F'Department={department}')
                                        print(F'Student Names\tTheir fees'
                                              F'{studentname1}\t{studentfees1}'
                                              F'{studentname2}\t{studentfees2}'
                                              F'{studentname3}\t{studentfees3}'
                                              F'{studentname4}\t{studentfees4}'
                                              F'{studentname5}\t{studentfees5}')
                                        break
                                    elif accessdata == 'click2':
                                        print('Admin details')
                                        print(F'name={Name}')
                                        print(F'Email={Email}')
                                        print('Password=********')
                                        print(F'Mobile Number={Mobilenumber}')
                                        print(F'Position={position}')
                                        break
                                    elif accessdata == 'click3':
                                        print(F'Password={Password}')
                                        break
                                    else:
                                        print('\t\terror\t\t\nselect option again')
                                break
                            elif option1 == 'no':
                                print('thank you!!!')
                                break
                            else:
                                print('\t\terror\t\t\nselect option again')
                    elif option == 'no':
                        print('thank you!!!')
                        break
                    else:
                        print('\t\terror\t\t\nselect appropriate option')
                break
            else:
                print('Input error\n select option again')
                click = input('YES or NO :-')
        break
    elif selectoption == 'login':
        print('first register here')
        selectoption = 'registration'
    else:
        print('\n----------error----------\n-------wrong input-------')
        selectoption = input('write your selected option again:-')
