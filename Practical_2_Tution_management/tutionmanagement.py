Trainer1 = input('Enter maths trainer name:')
print(F'This is {Trainer1} id : 01\n')
Trainer2 = input('Enter python trainer name:')
print(F'This is {Trainer2} id : 02\n')
totalstudents1 = input(F'\nEnter total students in one month teach maths by {Trainer1}:')
totalstudents2 = input(F'Enter total students in one month teach python by {Trainer2}:')
Lectureby1 = int(input(F'\nEnter taken lectures in month by {Trainer1}:'))
Lectureby2 = int(input(F'Enter taken lectures in month by {Trainer2}:'))

salary1 = 10000
if Lectureby1 >= 12:
    totalsalary1 = salary1 + 5000
else:
    totalsalary1 = salary1 - 2000
salary2 = 15000
if Lectureby2 >= 16:
    totalsalary2 = salary2 + 10000
else:
    totalsalary2 = salary2 - 8000

TA1 = totalsalary1 * 0.1
DA1 = totalsalary1 * 0.07
HRA1 = totalsalary1 * 0.2
PF1 = totalsalary1 * 0.18
totalincome1 = totalsalary1 + TA1 + DA1 + HRA1 - PF1

TA2 = totalsalary1 * 0.1
DA2 = totalsalary1 * 0.07
HRA2 = totalsalary1 * 0.2
PF2 = totalsalary1 * 0.18
totalincome2 = totalsalary2 + TA2 + DA2 + HRA2 - PF2

print('select options from below'.center(50, '*'))
while True:
    str2 = '\t_$_ for total income\t''_info_ for trainer information\t'
    print(str2.center(40, '*'))
    option = input('\nEnter your selected option here:')
    if option == '$' or option == '_$_':
        print('\nselect trainer by name or id')
        while True:
            Trainer = input('\nEnter trainer name or id or show all:')
            if Trainer == Trainer1 or Trainer == '01':
                dict1 = {'Name': Trainer1,
                         'Total income': totalincome1}
                print('\n', dict1)
                print('\ndo you want to continue search another trainer income')
                print('\nif yes then select trainer else enter -no-')
            elif Trainer == Trainer2 or Trainer == '02':
                dict2 = {'Name': Trainer2,
                         'Total income': totalincome2}
                print('\n', dict2)
                print('\ndo you want to continue search another trainer income')
                print('\nif yes then select trainer else enter -no-')
            elif Trainer == 'show all':
                dict1 = {'Name': Trainer1,
                         'Total income': totalincome1}
                dict2 = {'Name': Trainer2,
                         'Total income': totalincome2}
                print('\n', dict1)
                print('\n', dict2)
                print('\ndo you want to continue search another trainer income')
                print('\nif yes then select trainer else enter -no-')
            elif Trainer == 'no':
                str3 = 'Thank you!!!'
                print(str3.center(50, '*'))
                break
            else:
                print('\nselect appropriate option!!!')
        print('\ndo you want to continue get another information')
        print('\nif yes the select option from below else select -no-')
    elif option == 'info' or option == '_info_':
        print('\nselect trainer by name or id')
        while True:
            Trainer = input('\nEnter trainer name or id or show all:')
            if Trainer == Trainer1 or Trainer == '01':
                dict3 = {'Subject': 'Maths',
                         'Name': Trainer1,
                         'Trainer id': '01',
                         'Taken lecture in one month': Lectureby1}
                print('\n', dict3)
                print('\ndo you want to continue search another trainer information')
                print('\nif yes then select trainer else enter -no-')
            elif Trainer == Trainer2 or Trainer == '02':
                dict4 = {'Subject': 'Python',
                         'Name': Trainer2,
                         'Trainer id': '01',
                         'Taken lecture in one month': Lectureby2}
                print('\n', dict4)
                print('\ndo you want to continue search another trainer information')
                print('\nif yes then select trainer else enter -no-')
            elif Trainer == 'show all':
                dict3 = {'Subject': 'Maths',
                         'Name': Trainer1,
                         'Trainer id': '01',
                         'Taken lecture in one month': Lectureby1}
                dict4 = {'Subject': 'Python',
                         'Name': Trainer2,
                         'Trainer id': '01',
                         'Taken lecture in one month': Lectureby2}
                print('\n', dict3)
                print('\n', dict4)
                print('\ndo you want to continue search another trainer information')
                print('\nif yes then select trainer else enter -no-')
            elif Trainer == 'no':
                str3 = 'Thank you!!!'
                print(str3.center(50, '*'))
                break
            else:
                print('\nselect appropriate option!!!')
        print('\ndo you want to continue get another information')
        print('\nif yes the select option from below else select -no-')
    elif option == 'no':
        str3 = 'Thank you!!!'
        print(str3.center(50, '*'))
        break
    else:
        print('\nselect appropriate option!!!')
