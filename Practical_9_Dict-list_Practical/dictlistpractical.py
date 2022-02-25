print('\nEnter employee information down here\n')

Id1 = int(input('Enter employee id:'))
Name1 = input('Enter employee name:')
Salary1 = int(input('Enter employee salary:'))
TA1 = Salary1 * 0.1
DA1 = Salary1 * 0.07
HRA1 = Salary1 * 0.2
PF1 = Salary1 * 0.18

print('\nEnter new employee information down here\n')

dict1 = {'Employee id': Id1,
         'Employee name': Name1,
         'Employee salary': Salary1,
         'TA': TA1,
         'DA': DA1,
         'HRA': HRA1,
         'PF': PF1,
         'Total salary': Salary1 + TA1 + DA1 + HRA1 - PF1}

Id2 = int(input('Enter employee id:'))
Name2 = input('Enter employee name:')
Salary2 = int(input('Enter employee salary:'))
TA2 = Salary2 * 0.1
DA2 = Salary2 * 0.07
HRA2 = Salary2 * 0.2
PF2 = Salary2 * 0.18

print('\nEnter new employee information down here\n')

dict2 = {'Employee id': Id2,
         'Employee name': Name2,
         'Employee salary': Salary2,
         'TA': TA2,
         'DA': DA2,
         'HRA': HRA2,
         'PF': PF2,
         'Total salary': Salary2 + TA2 + DA2 + HRA2 - PF2}

Id3 = int(input('Enter employee id:'))
Name3 = input('Enter employee name:')
Salary3 = int(input('Enter employee salary:'))
TA3 = Salary3 * 0.1
DA3 = Salary3 * 0.07
HRA3 = Salary3 * 0.2
PF3 = Salary3 * 0.18

dict3 = {'Employee id': Id3,
         'Employee name': Name3,
         'Employee salary': Salary3,
         'TA': TA3,
         'DA': DA3,
         'HRA': HRA3,
         'PF': PF3,
         'Total salary': Salary3 + TA3 + DA3 + HRA3 - PF3}

dictwithlist = {'alldata': [dict1, dict2, dict3]}

for x in dictwithlist['alldata']:
    print(x)
