Salesmanname = input('Salesman name:-')
Salesmanid = input('Salesman id:-')
Laptopssold = int(input('Laptops sold:-'))
Mousesold= int(input('Mouse sold:-'))
commision= (Laptopssold*50000*0.05) + (Mousesold*500*0.05)
salary = 10000
Totalsalarywithcommision = salary + commision
print('******************************************************')
print('Joining date:-1/1/2020          Current date:-1/1/2022')
print('*********************Sales report*********************')
print(F'Salesman name:-{Salesmanname}          Salesman id:-{Salesmanid}')
print('***************shop name:- ONE FOR ALL****************')
print(F'Laptops sold:-{Laptopssold}')
print(F'Mouse sold:-{Mousesold}')
print('******************************************************')
print(F' Total commision = {commision}')
print(F'+Salary = {salary}')
print(F' Total salary = {Totalsalarywithcommision}')
print('******************************************************')



#count commision on each item
#item 1 laptop on each 5% commision
##item 2 mouse on each 5% commision
#enter = total quantity for each product
#and gives commision on each quantity
#find total salary and total commision
#final print the sales report with name and shop name